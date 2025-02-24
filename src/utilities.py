
import re
time_expression = re.compile(r"(\d{1,2}(?:am|pm))")
def clean_fish_entry(fish_entry):

    seasons = clean_seasons(fish_entry["Seasons"])
    time = clean_time(fish_entry["Time"])
    fish_entry["Seasons"] = seasons
    fish_entry["Time"] = time
    return fish_entry
def clean_time(time_entries:list):

    for i,time_entry in enumerate(time_entries):
        cleaned_entry= re.findall(time_expression,time_entry)
        if time_entries[0] == "Any":
            time_entries[0] = (6,2)
            break
        if cleaned_entry:
            time_lst= []
            for time in cleaned_entry:

                pm_modifier=0
                if "pm" in time:
                    pm_modifier= 12
                num = re.findall(r"(\d{1,2})",time)
                num = int(num[0]) +pm_modifier
                time_lst.append(num)
            time_entries[i] = (time_lst[0],time_lst[1])
        else:
            time_entries.pop(i)

    return time_entries
def clean_seasons(season_entries:list):
    seasons = {'Spring':-1,'Summer':-1,'Fall':-1,'Winter':-1,'All':-1}
    if "All" in season_entries and len(season_entries) <1:
        season_entries = season_entries[0:season_entries.index('All')]
        return season_entries
    for i,season_entry in enumerate(season_entries):
        if season_entry in seasons.keys() and seasons[season_entry]<=-1:
            seasons[season_entry]+=2
            continue
        season_entries = season_entries[0:i-1]
    return season_entries
