#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:25:11 2021

@author: cynding
"""
# %% Web scrapping - initialization

# Step 1 - Import
from selenium import webdriver
import pandas as pd
import re

# Step 2 - Access WebDriver
driver = webdriver.Chrome('/Users/cynding/Downloads/chromedriver 2')

hotel_list = ('sfoac-fairfield-inn-and-suites-napa-american-canyon', 
              'mcoat-residence-inn-orlando-altamonte-springs-maitland',
              'atlph-courtyard-atlanta-alpharetta',
              'nycsm-springhill-suites-new-york-midtown-manhattan-fifth-avenue',
              'avlac-ac-hotel-asheville-downtown',
              'abits-towneplace-suites-abilene-northeast') 

# %% Web scrapping

df = pd.DataFrame(columns=['Customer','Member_Type','Traveler_Type','Date','Review','Total_Score',
                           'Cleanliness','Dining','Location','Service','Amenities','Value_for_Money', 'Hotel'])

for i in range(len(hotel_list)):
    url = 'https://www.marriott.com/hotels/hotel-reviews/' + hotel_list[i] + '/'
    hotel_name = hotel_list[i]

    driver.get(url)
    
    member_type_list = []
    traveler_type_list = []
    date_list = []
    customers = []
    date_list = []
    reviews = []
    total_score_list = []
    cleanliness_score_list = []
    dining_score_list = []
    location_score_list = []
    service_score_list = []
    amenities_score_list = []
    valuefmoney_score_list = []
    
    nextpage = True
    while nextpage:
        readmore = True
    
    # click the 'readmore' button
        while readmore:
            try:
                driver.find_element_by_xpath('//span[@class="BVDI_AbbreviatedLink"]').click()
            except:
                readmore = False
    
        # extract the critical information
        for i in range(len(driver.find_elements_by_xpath('//div[@class="BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVRRDisplayContentReviewEven BVRREven"]'))):
            review_info = driver.find_elements_by_xpath('//div[@class="BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVRRDisplayContentReviewEven BVRREven"]')[i].text
            temp_series = pd.Series(review_info)
            
            member_type = temp_series.str.extract('(?:.*Member Level:)([a-zA-Z]+)(?:\n)')
            member_type = member_type.iloc[0].item()
            member_type_list.append(member_type)
            
            traveler_type = temp_series.str.extract('(?:.*Traveler Type:)([a-zA-Z]+)(?:\n)')
            traveler_type = traveler_type.iloc[0].item()
            traveler_type_list.append(traveler_type)
            
            date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)(\.)?(\w*)?(\.)?(\s*\d{0,2}\s*),(\s*\d{4})'
            date = re.search(date_pattern, review_info).group(0)
            date_list.append(date)
            
            # get the scores
            total_score = temp_series.str.extract('(?:.*Total score \n)([0-9]+[.]+[0-9])(?:\n)')
            total_score = total_score.iloc[0].item()
            total_score_list.append(total_score)
            
            cleanliness_score = temp_series.str.extract('(?:.*Cleanliness \n)([0-9]+[.]+[0-9])(?:\n)')
            cleanliness_score = cleanliness_score.iloc[0].item()
            cleanliness_score_list.append(cleanliness_score)
            
            dining_score = temp_series.str.extract('(?:.*Dining \n)([0-9]+[.]+[0-9])(?:\n)')
            dining_score = dining_score.iloc[0].item()
            dining_score_list.append(dining_score)
            
            location_score = temp_series.str.extract('(?:.*Location \n)([0-9]+[.]+[0-9])(?:\n)')
            location_score = location_score.iloc[0].item()
            location_score_list.append(location_score)
            
            service_score = temp_series.str.extract('(?:.*Service \n)([0-9]+[.]+[0-9])(?:\n)')
            service_score = service_score.iloc[0].item()
            service_score_list.append(service_score)
            
            amenities_score = temp_series.str.extract('(?:.*Amenities \n)([0-9]+[.]+[0-9])(?:\n)')
            amenities_score = amenities_score.iloc[0].item()
            amenities_score_list.append(amenities_score)
            
            valuefmoney_score = temp_series.str.extract('(?:.*Value for the Money \n)([0-9]+[.]+[0-9])(?:\n)')
            valuefmoney_score = valuefmoney_score.iloc[0].item()
            valuefmoney_score_list.append(valuefmoney_score)
            
            customers.append(review_info.split('\n')[0])
            
            if review_info.split('\n')[-5] != 'Read more': 
                reviews.append(review_info.split('\n')[-5])
            else:
               reviews.append(review_info.split('\n')[-6])
               
        
        for i in range(len(driver.find_elements_by_xpath('//div[@class="BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVRRDisplayContentReviewOdd BVRROdd"]'))):
            review_info = driver.find_elements_by_xpath('//div[@class="BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVRRDisplayContentReviewOdd BVRROdd"]')[i].text
            temp_series = pd.Series(review_info)
            
            member_type = temp_series.str.extract('(?:.*Member Level:)([a-zA-Z]+)(?:\n)')
            member_type = member_type.iloc[0].item()
            member_type_list.append(member_type)
            
            traveler_type = temp_series.str.extract('(?:.*Traveler Type:)([a-zA-Z]+)(?:\n)')
            traveler_type = traveler_type.iloc[0].item()
            traveler_type_list.append(traveler_type)
            
            date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)(\.)?(\w*)?(\.)?(\s*\d{0,2}\s*),(\s*\d{4})'
            date = re.search(date_pattern, review_info).group(0)
            date_list.append(date)
            
            # get the scores
            total_score = temp_series.str.extract('(?:.*Total score \n)([0-9]+[.]+[0-9])(?:\n)')
            total_score = total_score.iloc[0].item()
            total_score_list.append(total_score)
            
            cleanliness_score = temp_series.str.extract('(?:.*Cleanliness \n)([0-9]+[.]+[0-9])(?:\n)')
            cleanliness_score = cleanliness_score.iloc[0].item()
            cleanliness_score_list.append(cleanliness_score)
            
            dining_score = temp_series.str.extract('(?:.*Dining \n)([0-9]+[.]+[0-9])(?:\n)')
            dining_score = dining_score.iloc[0].item()
            dining_score_list.append(dining_score)
            
            location_score = temp_series.str.extract('(?:.*Location \n)([0-9]+[.]+[0-9])(?:\n)')
            location_score = location_score.iloc[0].item()
            location_score_list.append(location_score)
            
            service_score = temp_series.str.extract('(?:.*Service \n)([0-9]+[.]+[0-9])(?:\n)')
            service_score = service_score.iloc[0].item()
            service_score_list.append(service_score)
            
            amenities_score = temp_series.str.extract('(?:.*Amenities \n)([0-9]+[.]+[0-9])(?:\n)')
            amenities_score = amenities_score.iloc[0].item()
            amenities_score_list.append(amenities_score)
            
            valuefmoney_score = temp_series.str.extract('(?:.*Value for the Money \n)([0-9]+[.]+[0-9])(?:\n)')
            valuefmoney_score = valuefmoney_score.iloc[0].item()
            valuefmoney_score_list.append(valuefmoney_score)
            
            customers.append(review_info.split('\n')[0])
            if review_info.split('\n')[-5] != 'Show less': 
                reviews.append(review_info.split('\n')[-5])
            else:
               reviews.append(review_info.split('\n')[-6])
               
        # click the 'nextpage' button
        try:
            driver.find_element_by_xpath('//span[@class="BVRRPageLink BVRRNextPage"]').click()
        except:
            nextpage = False
    
    
    data_tuples = list(zip(customers[:],member_type_list[:],traveler_type_list[:],date_list[:],reviews[:],total_score_list[:],cleanliness_score_list[:],dining_score_list[:],location_score_list[:],service_score_list[:],amenities_score_list[:],valuefmoney_score_list[:]))
    temp_df = pd.DataFrame(data_tuples, columns=['Customer','Member_Type','Traveler_Type','Date','Review','Total_Score','Cleanliness','Dining','Location',
                                                     'Service','Amenities','Value_for_Money']) # creates dataframe of each tuple in list
    
    temp_df['Hotel'] = hotel_name
    df = df.append(temp_df)


# %%

df.to_csv('/Users/cynding/Desktop/marriott_hotel_reviews.csv', index=False)
driver.close()



