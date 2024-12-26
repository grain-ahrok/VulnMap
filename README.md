# VulnMap
Shodan API 를 사용하여 IoT 기기의 취약점을 수집하고 Map에 나타내어 분석을 돕는 도구입니다. VulnMap에서 IoT장치 이름을 검색하면 해당 장치의 노출된 취약점 빈도를 시각적으로 표시합니다. 최대 두 가지 장치에 대한 검색 결과를 지도에 표시할 수 있고 국가 코드를 활용해 특정 국가로 검색 범위를 제한할 수 있습니다.
<img width="733" alt="스크린샷 2024-12-18 오후 7 21 55" src="https://github.com/user-attachments/assets/52070796-5348-492f-9141-bd753b4d8fa4" />
<br/>

# VulnMap 사용방법
## API 키 입력
```
# Shodan API 키
API_KEY = "${SHODAN_API_KEY}"
api = shodan.Shodan(API_KEY)
```
shodan_location.py에서 ${SHODAN_API_KEY} 계정 API 키를 입력합니다.

```
<!-- Google Map API 키 -->
<script async defer 
   src="https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAP_API_KEY}">
</script>
```
shodan_map.html에서 ${GOOGLE_MAP_API_KEY} 계정 API 키를 입력합니다. 
<br/>

## 검색 실행
```
$ python shodan_location.py
```

<img width="452" alt="image" src="https://github.com/user-attachments/assets/94a6d673-8cf6-4bd2-b59b-538068b9aba8" /><br/>
python 스크립트를 실행하고 사진과 같이 입력하여 검색결과를 output.json과 output2.json 파일로 저장합니다.
<br/><br/>

<img width="733" alt="image" src="https://github.com/user-attachments/assets/aef85c6c-01f8-4e66-be5e-e04da7ef3243" /><br/>
완료되면 shodan_map.html 파일을 살행하여 아래와 같이 실행되는 것을 확인할 수 있습니다.
<br/><br/>

<img width="733" alt="image" src="https://github.com/user-attachments/assets/b0de77aa-d7eb-4721-9b0a-204d43844216" />
<br/>
마우스를 올려 해당 IP의 취약점 정보를 확인할 수 있습니다. 또, 클릭하여 IP에 대한 상세정보를 쇼단 페이지에서 확인할 수 있습니다.

