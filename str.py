
import json
import re
import requests
import ipaddress
import streamlit as st
from typing import List, Dict, Any

# --- Configuration ---
AZURE_JSON_FILE = "ServiceTags_Public_20251028.json"
MICROSOFT_URL = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    )
}

IPV4_REGEX = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# --- Load Azure IP Data ---
@st.cache_data(show_spinner=False)
def load_azure_data() -> Dict[str, Any]:
    """Load Azure IP ranges JSON from file."""
    try:
        with open(AZURE_JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"Azure IP list file '{AZURE_JSON_FILE}' not found.")
        st.stop()


# --- Utility Functions ---
def get_latest_json_url() -> str:
    """Extract latest Azure IP list JSON URL from Microsoft's confirmation page."""
    response = requests.get(MICROSOFT_URL, headers=HEADERS, timeout=10)
    match = re.search(r"https://download\.microsoft\.com/download[^\s\"']*?\.json", response.text.lower())
    return match.group(0) if match else ""


def extract_ips_from_text(text: str) -> List[str]:
    """Return all IPv4 addresses found in text."""
    return re.findall(IPV4_REGEX, text)


def is_valid_subnet(subnet: str) -> bool:
    """Check if string represents a valid IPv4 subnet."""
    try:
        ipaddress.IPv4Network(subnet, strict=False)
        return True
    except ValueError:
        return False


def ip_in_subnet(ip_str: str, subnet_str: str) -> bool:
    """Check if an IP address belongs to a given subnet."""
    try:
        ip = ipaddress.IPv4Address(ip_str)
        network = ipaddress.IPv4Network(subnet_str, strict=False)
        return ip in network
    except:
        return False

@st.cache_data(show_spinner=False)
def check_ip_in_azure(ip_to_check: str, data: Dict[str, Any]) -> List[str]:
    """Check whether an IP exists in the Azure IP ranges."""
    matches = []
    for entry in data.get("values", []):
        for prefix in entry["properties"].get("addressPrefixes", []):
            if is_valid_subnet(prefix) and ip_in_subnet(ip_to_check, prefix):
                matches.append(f"{prefix} → {entry['id']}")
    return matches


# --- Streamlit UI ---
st.set_page_config(page_title="IP Extractor", layout="centered")
st.title("🔍 Azure IP Address Checker")

st.markdown(
    """
    Paste any text below — this tool will extract all IPv4 addresses  
    and check if they belong to Azure’s public IP ranges.
    """
)

def ip_info(pubip):
    info = requests.get(f"http://ip-api.com/json/{pubip}")
    print(info)
    return info.json()
text_input = st.text_area("Enter text containing IP addresses:")
azure_data = load_azure_data()

# st.download_button(AZURE_JSON_FILE,AZURE_JSON_FILE, mime="json")
st.info(AZURE_JSON_FILE)
if st.button("🔎 Extract & Check IPs"):


    if not text_input.strip():
        st.warning("Please enter some text first.")
    else:
        found_ips = extract_ips_from_text(text_input)
        if not found_ips:
            st.info("No IP addresses found.")
        else:
            st.success(f"Found {len(found_ips)} IP address(es):")
            for ip in found_ips:
                results = check_ip_in_azure(ip, azure_data)
                if results:
                    st.write(f"✅ **{ip}** is found in Azure ranges:")
                    for match in results:
                        st.code(match, language="text")
                else:
                    st.write(f"❌ **{ip}** not found in Azure ranges. - {ip_info(ip)}")