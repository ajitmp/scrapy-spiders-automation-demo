import json
from jinja2 import Environment, FileSystemLoader
from urllib.parse import urlparse
import os

# Load JSON configuration
with open('sources.json') as f:
    config = json.load(f)

# Extract values and manipulate strings
spidername = config['spidername'].title().replace(" ", "")
spiderclass = spidername.capitalize()+'Spider'
start_urls = config['start_urls']
parsed_url = urlparse(start_urls[0])
allowed_domains = parsed_url.netloc

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('spiders_automation_demo/templates/spiders/'))
template = env.get_template('quotespider_template.jinja2')

# Render the template with values
output = template.render(
    spiderclass=spiderclass,
    spidername=spidername,
    allowed_domains=allowed_domains,
    start_urls=start_urls,
    quote_div_main=config['quote_div_main'],
    title_selector=config['title_selector'],
    author_selector=config['author_selector']
)

# Folder where you want to save the spider file
folder_name = 'spiders_automation_demo/spiders'

# Ensure the folder exists
os.makedirs(folder_name, exist_ok=True)

# Save the rendered template to a new Python file in the specified folder
file_path = os.path.join(folder_name, f'{spiderclass}.py')
with open(file_path, 'w') as f:
    f.write(output)

print(f"Spider generated: {file_path}")
