import shodan
import json


# Shodan API 키
API_KEY = "{API_KEY}"
api = shodan.Shodan(API_KEY)


# 상품 이름
product = input("insert product name : ")
product = product.strip()
# 도시
country = input("insert country code : ")
country = country.strip()

# 쿼리문 생성
if country == '' :
    query = f'product:{product}'
else :
    query = f'product:{product} country:{country}'

try:
    results = api.search(query)
    print(f"Results found: {results['total']}")
    with open("output.json", "w", encoding="utf-8") as output_file:
        json.dump(results, output_file, indent=4, ensure_ascii=False)
    print("Results have been saved to output.json.")
except shodan.APIError as e:
    print(f"Shodan API Error: {e}")

print("output.json file creation complete")


ui = input("Are you going to input second product? (y/n): ")
if ui.lower() not in ['y', 'yes']:
    exit(1)


# 상품 이름
product2 = input("insert product name : ")
product2 = product2.strip()
# 도시
country2 = input("insert country code : ")
country2 = country2.strip()

# 쿼리문 생성
if country2 == '' :
    query2 = f'product:{product2}'
else :
    query2 = f'product:{product2} country:{country2}'

try:
    results = api.search(query2)
    print(f"Results found: {results['total']}")
    with open("output2.json", "w", encoding="utf-8") as output_file:
        json.dump(results, output_file, indent=4, ensure_ascii=False)
    print("Results have been saved to output2.json.")
except shodan.APIError as e:
    print(f"Shodan API Error: {e}")


print("output2.json file creation complete")
print("You can open the shodan_map.html file in a browser to view the data.")
