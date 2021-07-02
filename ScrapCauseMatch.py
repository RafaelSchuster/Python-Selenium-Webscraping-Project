from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import webbrowser
import time
import json
from natsort import humansorted

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.causematch.com/")

data_dict = {}


def element_by_css_selector(identifier):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, identifier))
    )


def vars_assignment(donor_sel, donation_sel):
    donor = element_by_css_selector(donor_sel)
    donation = element_by_css_selector(donation_sel)
    data_dict[donation.text.replace(',', '')] = {
        driver.current_url: donor.text}


def data_storing_with_for_loop(starter):
    for k in range(starter, 15, 1):
        try:
            vars_assignment('#rdp-card-list > div:nth-child(%s) > div > div.media.rdp-item-row > div.media-body.rdp-item-details > h5' % (
                str(k)), '#rdp-card-list > div:nth-child(%s) > div > div.media.rdp-item-row > div.media-body.rdp-item-details > h4' % (str(k)))
        except:
            vars_assignment('#rdp-card-list > div:nth-child(%s) > div > div > div.media-body.rdp-item-details > h5' % (str(k)),
                            '#rdp-card-list > div:nth-child(%s) > div > div > div.media-body.rdp-item-details > h4' % (str(k)))


def default_pass():
    print(' ')


def campaign_loop(start, end, button_action=default_pass):
    try:
        for i in range(start, end, 1):
            campaign = element_by_css_selector(
                '#container > div:nth-child(%s) > a > div > div > img' % (str(i)))
            campaign.click()
            try:
                donors_tab = element_by_css_selector(
                    '#content-donors-tab')
                donors_tab.click()
                selection = element_by_css_selector(
                    '#donors-tab > div.rdp-data-container > div > div.rdp-sn-container.row > div.tc-filter-container.col-sm-3 > div')
                selection.click()

                option = element_by_css_selector(
                    '#donors-tab > div.rdp-data-container > div > div.rdp-sn-container.row > div.tc-filter-container.col-sm-3 > div > div > a:nth-child(2)')
                option.click()
            except:
                try:
                    out_click = element_by_css_selector(
                        '#vm-mdd > div > div > button')

                    out_click.click()
                    selection = element_by_css_selector(
                        '#donors-tab > div.rdp-data-container > div > div.rdp-sn-container.row > div.tc-filter-container.col-sm-3 > div')

                    selection.click()

                    option = element_by_css_selector(
                        '#donors-tab > div.rdp-data-container > div > div.rdp-sn-container.row > div.tc-filter-container.col-sm-3 > div > div > a:nth-child(2)')
                    option.click()
                except:
                    try:
                        donors_tab = element_by_css_selector(
                            '#content-donors-tab')
                        donors_tab.click()
                        selection = element_by_css_selector(
                            '#donors-tab > div.rdp-data-container > div > div.rdp-sn-container.row > div.tc-filter-container.col-sm-3 > div')

                        selection.click()

                        option = element_by_css_selector(
                            '#donors-tab > div.rdp-data-container > div > div.rdp-sn-container.row > div.tc-filter-container.col-sm-3 > div > div > a:nth-child(2)')
                        option.click()
                    except:
                        driver.back()
                        button_action()
                        continue
            try:
                data_storing_with_for_loop(1)
                driver.back()
                button_action()
            except:
                data_storing_with_for_loop(2)
                driver.back()
                button_action()
        driver.back()
        button_action()
    except:
        print('Final Result For Now:')
        print(humansorted(data_dict.items(), reverse=True))
        data = humansorted(data_dict.items(), reverse=True)
        json_string = json.dumps(data, ensure_ascii=False)
        time.sleep(3)
        html_content_end = f"<html><head></head><h1>Scrapping Results</h1><body>{json_string}</body></html>"
        with open("index.html", "w", encoding='utf-8') as html_file:
            html_file.write(html_content_end)
            print('HTML file created successfully!')
        time.sleep(5)
        webbrowser.open_new_tab("index.html")


def israel_button():
    israel = element_by_css_selector('#filters > div > ul > li:nth-child(2)')
    israel.click()


def usa_button():
    usa = element_by_css_selector('#filters > div > ul > li:nth-child(3)')
    usa.click()


def uk_button():
    uk = element_by_css_selector('#filters > div > ul > li:nth-child(4)')
    uk.click()


def panama_button():
    panama = element_by_css_selector('#filters > div > ul > li:nth-child(5)')
    panama.click()


def more_button():
    more = element_by_css_selector('#filters > div > ul > li:nth-child(6)')
    more.click()


number_trending_campaigns = len(driver.find_elements_by_class_name('trending'))
number_israel_campaigns = len(driver.find_elements_by_class_name('israel'))
number_usa_campaigns = len(driver.find_elements_by_class_name('usa'))
number_uk_campaigns = len(driver.find_elements_by_class_name('uk'))
number_panama_campaigns = len(driver.find_elements_by_class_name('panama'))
number_more_campaigns = len(driver.find_elements_by_class_name('more'))

israel_start = number_trending_campaigns + 1
israel_end = number_trending_campaigns + number_israel_campaigns

usa_start = number_trending_campaigns + number_israel_campaigns + 1
usa_end = number_trending_campaigns + \
    number_israel_campaigns + number_usa_campaigns

uk_start = number_trending_campaigns + \
    number_israel_campaigns + number_usa_campaigns + 1
uk_end = number_trending_campaigns + number_israel_campaigns + \
    number_usa_campaigns + number_uk_campaigns

panama_start = number_trending_campaigns + number_israel_campaigns + \
    number_usa_campaigns + number_uk_campaigns + 1
panama_end = number_trending_campaigns + number_israel_campaigns + \
    number_usa_campaigns + number_uk_campaigns + number_panama_campaigns

more_start = number_trending_campaigns + number_israel_campaigns + \
    number_usa_campaigns + number_uk_campaigns + number_panama_campaigns + 1
more_end = number_trending_campaigns + number_israel_campaigns + number_usa_campaigns + \
    number_uk_campaigns + number_panama_campaigns + number_more_campaigns

print(number_trending_campaigns, number_israel_campaigns, number_usa_campaigns,
      number_uk_campaigns, number_panama_campaigns, number_more_campaigns)

campaign_loop(1, number_trending_campaigns)
print(humansorted(data_dict.items(), reverse=True))

driver.get("https://www.causematch.com/")

usa_button()
campaign_loop(usa_start, usa_end, usa_button)
print(humansorted(data_dict.items(), reverse=True))

driver.get("https://www.causematch.com/")

uk_button()
campaign_loop(uk_start, uk_end, uk_button)
print(humansorted(data_dict.items(), reverse=True))

driver.get("https://www.causematch.com/")

panama_button()
campaign_loop(panama_start, panama_end, panama_button)
print(humansorted(data_dict.items(), reverse=True))

driver.get("https://www.causematch.com/")

more_button()
print(more_start)
campaign_loop(more_start, more_end, more_button)
print(humansorted(data_dict.items(), reverse=True))

driver.get("https://www.causematch.com/")

israel_button()
campaign_loop(israel_start,
              israel_end, israel_button)
print(humansorted(data_dict.items(), reverse=True))

time.sleep(3)
data = humansorted(data_dict.items(), reverse=True)
json_string = json.dumps(data, ensure_ascii=False)
html_content_end = f"<html><head></head><h1>Scrapping Results</h1><body>{json_string}</body></html>"
with open("index.html", "w", encoding='utf-8') as html_file:
    html_file.write(html_content_end)
    print('HTML file created successfully!')
time.sleep(5)
webbrowser.open_new_tab("index.html")
