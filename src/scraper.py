from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, Tag
import json
from utilities import clean_fish_entry
base_url="https://stardewvalleywiki.com"
fish_url = base_url + "/Fish"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
fish_structure = {"locations":[],"seasons":[],"weather":[],"time":[()]}
def get_fish_nav_table(soup):
    fish_table = soup.find("table", {"id": "navbox"})
    return fish_table
def filter_row(tag:Tag):
    return tag.name == "tr" and tag.td is not None
def filter_fish_row(tag:Tag):
    return tag.name == "tr" and tag.find_next("td").string is not None and tag.find_next("td").string.strip() in ["Location", "Time", "Season", "Weather"]
def get_location_fish_rows(soup):
    fish_location_dict = {}
    rows_to_traverse = soup.find_all(filter_row)
    for row in rows_to_traverse:
        location = row.th.text.strip()
        fish_cells = row.find("td")
        for cell in fish_cells.find_all("a"):
            if cell.text not in fish_location_dict.keys():

                fish_name = cell.text
                if location in ["Crab Pot"]:
                    fish_name = f"{location} {fish_name}"
                fish_location_dict[fish_name] = []
    return fish_location_dict
def filter_anchors(tag:Tag):
    return tag.name == "a"
def get_info_section_by_name( soup, name):
        info_table = soup.find(id='infoboxtable')

        info_box_sections = info_table.find_all(id='infoboxsection')
        for box_section in info_box_sections:
            if box_section.text.strip() == name:
                parent_tr = box_section.find_parent('tr')
                details = parent_tr.find(id='infoboxdetail')
                return details
        return None

# def get_fish_info(fish_name):
#     fish_name = "/"+fish_name.replace(" ", "_")
#     soup = BeautifulSoup(urlopen(Request(base_url+fish_name, headers=headers)).read(), "html.parser")
#     table = soup.find("table", {"id": "infoboxtable"})
#     rows = table.find_all(filter_fish_row)
#     locations,seasons,weather = [],[],[]
#     time = ""
#     LOCATION = 0
#     TIME = 1
#     SEASON =2
#     WEATHER =3
#     for x in range(len(rows)):
#         row = rows[x]
#         links = row.find_all("a")
#         if links:
#             object =  [link.text for link in links]
#             if x == LOCATION:
#                 locations = object
#             elif x == SEASON:
#                 seasons = object
#             elif x == WEATHER:
#                 weather = object
#         else:
#             time = row.find_all("td")[1].text.strip()
#     if 'Ginger Island' in seasons and 'All' in seasons:
#         seasons.remove('All')
#         seasons.remove('Ginger Island')
#     if 'All' in seasons:
#         seasons.remove('All')
#         seasons.append('All Seasons')
#     fish = Fish.Fish()
#     fish.name = fish_name.replace("_", " ").replace("/", "")
#     fish.locations = locations
#     fish.time = time
#     fish.seasons = seasons
#     fish.weather = weather
#     return fish
def handle_link_or_string(soup):
        contents_list = []
        # TODO look for bullet as a separator and string those words together

        string_builder = []
        for item in soup.contents:
            item_soup = BeautifulSoup(str(item), 'html.parser')
            if item_soup.find_all('a'):
                [string_builder.append(contents.get_text()) for contents in item_soup.find_all('a') if contents.get_text() != '']
            elif item_soup.find_all('li'):
                [string_builder.append(contents.get_text()) for contents in item_soup.find_all('li') if contents.get_text() != '']
            else:
                if item_soup.contents[0]:
                    # skip images
                    img_soup = BeautifulSoup(str(item_soup), 'html.parser')
                    if img_soup.find('img') or img_soup.find('br'):
                        continue

                    # We have found a word separator. add string builder to contents_list joined.
                    # if '•' in item_soup.contents[0]:
                    #     contents_list.append(' '.join(string_builder))
                        #string_builder = []

                    # strip out special characters

                    contents = item_soup.contents[0].replace('•', '').replace('–', 'to').replace('-', 'to').replace('\u2013','to').strip()

                    if contents != '':
                        string_builder.append(contents)

        # if there was only one option and there is no word separator bullet
        if len(string_builder) != 0:
            contents_list.append(' '.join(string_builder))

       # contents = join_list_human_readable(contents_list)
        return string_builder

def join_list_human_readable(list_to_join):
        connector_string = ', and '

        # commas don't make sense if its only two things
        if len(list_to_join) == 2:
            connector_string = ' and '

        return ", ".join(list_to_join[:-2] + [connector_string.join(list_to_join[-2:])])

souper = BeautifulSoup(urlopen(Request(base_url+"/Fish", headers=headers)).read(), "html.parser")
fish_table = souper.find("table", {"id": "navbox"})
fish_table = get_fish_nav_table(souper)
fish_location_dict = get_location_fish_rows(fish_table)
file = open("fishes.json", "w")
fish_info = {}
for fish in fish_location_dict.keys():
    if "Crab Pot" in fish:
        continue
    fish_name = "/"+fish.replace(" ","_")
    soup = BeautifulSoup(urlopen(Request(base_url+fish_name, headers=headers)).read(), "html.parser")
    location_section = get_info_section_by_name(soup, 'Location')
    time_section = get_info_section_by_name(soup, 'Time')
    season_section = get_info_section_by_name(soup, 'Season')
    weather_section = get_info_section_by_name(soup, 'Weather')
    location_string = handle_link_or_string(location_section)
    season_string= handle_link_or_string(season_section)
    weather_string = handle_link_or_string(weather_section)
    time_string = handle_link_or_string(time_section)
    # if "Ginger Island" in season_string and "All" in season_string:

    #     season_string =  season_string.split("Ginger Island")[0]
    # if "All" in season_string:
    #     if "Winter" in season_string:
    #         season_string = season_string.split("All")[0].strip()
    #     elif "Fall" in season_string:
    #         season_string.split("Fall")
    #         season_string = season_string.split("All")[0].strip()
    #     elif "Spring" in season_string:
    #         season_string.split("Spring")
    #         season_string = season_string.split("All")[0].strip()
    #     elif "Summer" in season_string:
    #         season_string.split("Summer")
    #         season_string = season_string.split("All")[0].strip()
    fish_entry = {"Locations": location_string, "Time": time_string, "Seasons": season_string, "Weather": weather_string}
    clean_entry = clean_fish_entry(fish_entry)
    fish_info[fish] = clean_entry


json.dump(fish_info, file)
file.close()



    # location_list = location_string.replace("and","").strip().split(",")
    # for location in location_list:
    #    location = location.strip()
    #    season_string = season_string.replace("Anytime during "+location, "")
    # if "The" in season_string:
    #     season_string = season_string.replace("The", "").strip().replace("All","").strip()


# for fish_name, locations in fish_location_dict.items():
#     if "Crab Pot" in fish_name:
#         continue
#     fish = get_fish_info(fish_name)
#     print(fish)

