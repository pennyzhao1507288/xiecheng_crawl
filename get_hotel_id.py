"""
根据城市id，读取该城市的酒店id列表，并保存到txt文件中
"""
import random
import time

from repeat import remove_duplicate_lines
import requests

with open('ip1.txt', 'r') as file:
    proxy_list = [line.strip() for line in file]
def select_random_proxy(proxy_list):
    return random.choice(proxy_list)


def get_hotel_list(pageIndex,cityid):
    # 获取一个随机代理IP
    random_proxy = select_random_proxy(proxy_list)
    ip, port, username, password = random_proxy.split(':')
    proxy_url = f"http://{username}:{password}@{ip}:{port}"
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }
    burp0_url = "https://uk.trip.com:443/htls/getHotelList?testab=f59b0ade56203e4410b5d8d87110905a032b17de8b08325aa53f44ead3f9019e&x-traceID=1698077771987.63a4QEc5sdbB-1714134298779-1406268835"
    burp0_cookies = {"_abtest_userid": "275b5bfb-dc22-41fe-8cde-383654a6d102", "Union": "AllianceID=1052761&SID=1816122&OUID=ctag.hash.f79ac153df65&Expires=1716725994879&createtime=1714133994", "ibu_online_home_language_match": "{\"isRedirect\":false,\"isShowSuggestion\":false,\"lastVisited\":true,\"region\":\"gb\",\"redirectSymbol\":false,\"site_url\":[]}", "ibulanguage": "EN", "ibulocale": "en_gb", "cookiePricesDisplayed": "GBP", "ubtc_trip_pwa": "2", "ibu_oh_pp_exposed": "1", "_gid": "GA1.2.1601137272.1714133996", "_gac_UA-109672825-1": "1.1714133996.CjwKCAjwoa2xBhACEiwA1sb1BGLQgcaswF74HcyepuwxMqov0m69ctXUanS0yzSH__Kn14928cPAGBoCToMQAvD_BwE", "_gcl_au": "1.1.2052504540.1714133997", "_gac_UA-109672825-3": "1.1714133997.CjwKCAjwoa2xBhACEiwA1sb1BGLQgcaswF74HcyepuwxMqov0m69ctXUanS0yzSH__Kn14928cPAGBoCToMQAvD_BwE", "_fwb": "141IaqDmK0gAjmp6Hdt1Msl.1714133997010", "UBT_VID": "1698077771987.63a4QEc5sdbB", "_tt_enable_cookie": "1", "_ttp": "-H9KSPTTa5k5w5bsPDOZ0N7Yon-", "_combined": "transactionId%3De3aae1d944506c47385ebe8cf57be62d", "_gac_UA-109672825-13": "1.1714133998.CjwKCAjwoa2xBhACEiwA1sb1BGLQgcaswF74HcyepuwxMqov0m69ctXUanS0yzSH__Kn14928cPAGBoCToMQAvD_BwE", "_gcl_aw": "GCL.1714133998.CjwKCAjwoa2xBhACEiwA1sb1BGLQgcaswF74HcyepuwxMqov0m69ctXUanS0yzSH__Kn14928cPAGBoCToMQAvD_BwE", "_RF1": "130.88.226.3", "_RSG": "eVaClGMyB2DAnkG2IX81z8", "_RDG": "28bfcb44b1dbf72dcd1f3dc2a39ba5226d", "_RGUID": "d08bf164-2f32-47e8-8f41-22148242ec4a", "_tp_search_latest_channel_name": "hotels", "hotelhst": "1164390341", "ibu_hotel_search_date": "{\"checkIn\":\"2024/04/26\",\"checkOut\":\"2024/04/27\"}", "g_state": "{\"i_p\":1714141217568,\"i_l\":1}", "IBU_TRANCE_LOG_P": "37786417776", "devicePixelRatio": "1.25", "oldLocale": "en-GB", "_fbp": "fb.1.1714134021956.133231927", "ibu_online_permission_cls_ct": "1", "ibu_online_permission_cls_gap": "1714134025088", "GUID": "09031122114466466662", "nfes_isSupportWebP": "1", "_resDomain": "https%3A%2F%2Fak-s.tripcdn.com", "nfes_isSupportWebP": "1", "librauuid": "", "_bfa": "1.1698077771987.63a4QEc5sdbB.1.1714134032909.1714134068671.8.6.10320668148", "IBU_showtotalamt": "3", "_uetsid": "5a3c700003c711efbd52c395c64b9c06", "_uetvid": "88e6ed6071bf11eea429b3e2d9511144", "NA_SAC": "dT1odHRwcyUzQSUyRiUyRnVrLnRyaXAuY29tJTJGaG90ZWxzJTJGbGlzdCUzRmNpdHklM0QtMSUyNnByb3ZpbmNlSWQlM0Q1MyUyNmNvdW50cnlJZCUzRDElMjZkaXN0cmljdElkJTNEMCUyNmNoZWNraW4lM0QyMDI0JTJGMDQlMkYyNiUyNmNoZWNrb3V0JTNEMjAyNCUyRjA0JTJGMjclMjZiYXJDdXJyJTNER0JQJTI2c2VhcmNoVHlwZSUzRFAlMjZzZWFyY2hXb3JkJTNEJTI1RTUlMjU4RiUyNUIwJTI1RTclMjU4MSUyNUEzJTI2c2VhcmNoQ29vcmRpbmF0ZSUzREJBSURVXy0xXy0xXzAlN0NHQU9ERV8tMV8tMV8wJTdDR09PR0xFXy0xXy0xXzAlN0NOT1JNQUxfLTFfLTFfMCUyNmNybiUzRDElMjZhZHVsdCUzRDIlMjZjaGlsZHJlbiUzRDAlMjZzZWFyY2hCb3hBcmclM0R0JTI2dHJhdmVsUHVycG9zZSUzRDAlMjZjdG1fcmVmJTNEaXhfc2JfZGwlMjZkb21lc3RpYyUzRHRydWV8cj1odHRwcyUzQSUyRiUyRnVrLnRyaXAuY29tJTJGJTNGbG9jYWxlJTNEZW5fZ2IlMjZhbGxpYW5jZWlkJTNEMTA1Mjc2MSUyNnNpZCUzRDE4MTYxMjIlMjZwcGNpZCUzRGNraWQtMTA5OTI0NTExMDhfYWRpZC02ODg2MjEzMzQ3NjhfYWtpZC1rd2QtMTE2MzU3MjFfYWRnaWQtMTU5MDU4MDA2Nzc4JTI2dXRtX3NvdXJjZSUzRGdvb2dsZSUyNnV0bV9tZWRpdW0lM0RjcGMlMjZ1dG1fY2FtcGFpZ24lM0QyMDk1Njg3ODM2MyUyNmdhZF9zb3VyY2UlM0QxJTI2Z2NsaWQlM0RDandLQ0Fqd29hMnhCaEFDRWl3QTFzYjFCR0xRZ2Nhc3dGNzRIY3llcHV3eE1xb3YwbTY5Y3RYVWFuUzB5elNIX19LbjE0OTI4Y1BBR0JvQ1RvTVFBdkRfQndF", "wcs_bt": "s_33fb334966e9:1714134072", "_ga_37RNVFDP1J": "GS1.2.1714133996.1.1.1714134072.60.0.0", "_ga": "GA1.2.534275832.1714133996", "_ga_2DCSB93KS4": "GS1.2.1714133997.1.1.1714134074.59.0.0", "_ga_X437DZ73MR": "GS1.1.1714133997.1.1.1714134187.0.0.0"}
    burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"", "Currency": "GBP", "Locale": "en-GB", "Trip-Trace-Id": "1698077771987.63a4QEc5sdbB-1714134298779-1406268835", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36", "Sec-Ch-Ua-Mobile": "?0", "Content-Type": "application/json", "Accept": "application/json", "Pid": "e5aa3b8d-f4e5-442b-bf7e-d84994aca82d", "P": "37786417776", "X-Traceid": "1698077771987.63a4QEc5sdbB-1714134298779-1406268835", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://uk.trip.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://uk.trip.com/hotels/list?city=-1&provinceId=53&countryId=1&districtId=0&checkin=2024/04/26&checkout=2024/04/27&barCurr=GBP&searchType=P&searchWord=%E5%8F%B0%E7%81%A3&searchCoordinate=BAIDU_-1_-1_0|GAODE_-1_-1_0|GOOGLE_-1_-1_0|NORMAL_-1_-1_0&crn=1&adult=2&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=true", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    burp0_json={"batchRefresh": {"batchId": "", "batchSeqNo": 0}, "extends": {"crossPriceConsistencyLog": "", "enableDynamicRefresh": "T", "ExposeBedInfos": False, "isFirstDynamicRefresh": "T", "MealTagDependOnMealType": "T", "MultiMainHotelPics": "T", "NewTaxDescForAmountshowtype0": "", "TaxDescForAmountshowtype2": ""}, "guideLogin": "T", "head": {"aid": "1052761", "bu": "ibu", "caid": "1052761", "cid": "1698077771987.63a4QEc5sdbB", "clientId": "1698077771987.63a4QEc5sdbB", "clientVersion": "0", "couid": "ctag.hash.f79ac153df65", "csid": "1816122", "currency": "GBP", "deviceConfig": "M", "deviceID": "PC", "extension": [{"name": "cityId", "value": "-1"}, {"name": "checkIn", "value": "2024/04/26"}, {"name": "checkOut", "value": "2024/04/27"}], "frontend": {"pvid": "6", "sessionID": "8", "vid": "1698077771987.63a4QEc5sdbB"}, "group": "TRIP", "hotelExtension": {"hotelTestAb": "f59b0ade56203e4410b5d8d87110905a032b17de8b08325aa53f44ead3f9019e", "hotelUuidKey": ""}, "href": "https://uk.trip.com/hotels/list?city=-1&provinceId=53&countryId=1&districtId=0&checkin=2024/04/26&checkout=2024/04/27&barCurr=GBP&searchType=P&searchWord=%E5%8F%B0%E7%81%A3&searchCoordinate=BAIDU_-1_-1_0|GAODE_-1_-1_0|GOOGLE_-1_-1_0|NORMAL_-1_-1_0&crn=1&adult=2&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=true", "locale": "en-GB", "ouid": "ctag.hash.f79ac153df65", "p": "37786417776", "pageID": "10320668148", "pid": "e5aa3b8d-f4e5-442b-bf7e-d84994aca82d", "platform": "PC", "qid": 276143403844, "region": "GB", "sid": "1816122", "ticket": "", "timeZone": "8", "traceLogID": "1854f89da9931", "tripSub1": ""}, "mapType": "GOOGLE", "queryTag": "NORMAL", "search": {"checkIn": "20240426", "checkOut": "20240427", "crossPromotionId": "", "filters": [{"filterId": "17|1", "sceneType": "17", "subType": "2", "type": "17", "value": "1"}, {"filterId": "80|3|1", "sceneType": "80", "subType": "2", "type": "80", "value": "3"}, {"filterId": "29|1", "type": "29", "value": "1|2"}], "hotelId": 0, "hotelIds": [], "lat": 25.038613905324276, "lng": 121.55880701449858, "location": {"coordinates": [], "geo": {"cityID": cityid, "countryID": 1, "districtID": 0, "oversea": False, "provinceID": 53}}, "nearbyHotHotel": {}, "needTagMerge": "T", "orderFieldSelectedByUser": False, "pageCode": 10320668148, "pageIndex": pageIndex, "pageSize": 10, "recommendTimes": 0, "resultType": "P", "roomQuantity": 1, "sessionId": "6a7d4649-79b2-57ba-8ff9-82a70f8491b5", "sourceFromTag": "", "travellingForWork": False, "tripWalkDriveSwitch": "T"}}
    res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json,proxies=proxies)
    time.sleep(2)
    data = res.json()
    # print(data)
    # cityname  = data['positionInfo']['cityName']
    # ciytid = data['positionInfo']['cityId']
    hotelList = data['hotelList']
    hotel_ids = [item['hotelBasicInfo']['hotelId'] for item in hotelList]
    print(hotel_ids)
    return hotel_ids

def save_hotel_ids_to_txt(cityid):
    all_hotel_ids = []
    try:
        page_index = 1  # 从第一页开始
        # while len(all_hotel_ids) < target_count:
        while True:
            hotel_ids = get_hotel_list(page_index, cityid)
            print(f"Page {page_index} Hotel Info: {hotel_ids}")
            if not hotel_ids:  # 如果hotel_ids为空，表示已经没有更多酒店信息
                print("No more hotels found.")
                break
            all_hotel_ids.extend(hotel_ids)
            page_index += 1
    except Exception as e:
        print("读取完成,总共有",len(all_hotel_ids),"个酒店")
        print(e)

    # 将所有的 hotel_ids写入txt文件，以cityName命名
    txt_file_name = 'taipei.txt'
    with open(txt_file_name, 'w') as file:
        for hotel_id in all_hotel_ids:
            file.write(str(hotel_id) + '\n')

    file_path = txt_file_name  # 使用新生成的txt文件的路径
    remove_duplicate_lines(file_path)
    print(f"Hotel IDs saved to {txt_file_name}")
    return txt_file_name

# save_hotel_ids_to_txt(-1)
#吕宋岛0
#台北市-1