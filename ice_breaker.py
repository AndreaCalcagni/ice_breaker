import os
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.linkedin import scrape_linkedin_profile_gist
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import HuggingFaceHub

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

import re

if __name__ == "__main__":
    # linkedin_data = scrape_linkedin_profile_gist()

    summary_template = """
    given the Linkedin information {information} about a person, I want you to create:
    1. a summary of the person's profile
    2. two interesting facts about the person"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = linkedin_lookup_agent(name="Sara Calcagni")

    # clean URL
    pattern = r"https?://(?:[a-z]{2}\.)?linkedin\.com/in/([a-zA-Z0-9-]+)"
    match = re.search(pattern, linkedin_profile_url)
    username = match.group(1)
    linkedin_profile_url = f"https://linkedin.com/in/{username}"

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/sara-calcagni-9866a4173/')

    print(chain.run(information=linkedin_data))


# if __name__ == "__main__":

#     linkedin_data = scrape_linkedin_profile_gist()

#     summary_template = """
#     given the Linkedin information {information} about a person, I want you to create the following two paragraphs:
#     1. a summary of the person's profile
#     2. two interesting facts about the person"""

#     summary_prompt_template = PromptTemplate(
#         input_variables=['information'], template=summary_template)

#     repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

#     llm = HuggingFaceHub(
#     repo_id=repo_id, model_kwargs={"temperature": 0.1, "max_length": 500}
#     )

#     chain = LLMChain(llm=llm, prompt=summary_prompt_template)
#     print(chain.run(information=linkedin_data))
