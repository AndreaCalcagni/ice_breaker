import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from a linkedin profiles,
    Manually scrape the information from the linkedin profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, headers=header_dic, params={"url": linkedin_profile_url}
    )
    data = response.json()
    data = {
        key: value
        for key, value in data.items()
        if key
        not in [
            "people_also_viewed",
            "also_viewed",
            "people_also_viewed_urls",
            "also_viewed_urls",
            "certifications",
        ]
        and value not in ([], None, "")
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


def scrape_linkedin_profile_gist():
    """scrape information from a linkedin profiles,
    Manually scrape the information from the linkedin profile"""
    gist_response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    )
    data = gist_response.json()
    data = {
        key: value
        for key, value in data.items()
        if key
        not in [
            "people_also_viewed",
            "also_viewed",
            "people_also_viewed_urls",
            "also_viewed_urls",
            "certifications",
        ]
        and value not in ([], None, "")
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data
