
path = "lab\\week6\\weather.txt"

def read_file(path) :
    with open(path, "r", encoding="utf-8") as f :
        data = f.readlines()
        clean_data = []

        for line in data[5:] : #인덱스 오류가 있어서 수정요망.
            clean_line = line.strip().split(",")

            clean_data.append(
            {"날짜": clean_line[0], "지역": clean_line[1], 
             "평균기온": float(clean_line[2]), "최저기온": float(clean_line[3]),
             "최고기온": float(clean_data[4])}
            )

    return clean_data

clean_data = read_file(path)

most_cold = min(clean_data, key=lambda x : x["최저기온"]) #그냥 한 행 자체가 튀어나옴!

print(f"가장 추운 날씨는 {most_cold["최저기온"]}도였고, 그때는 {most_cold["날짜"]}이었습니다.")