import os
import csv

def scan_all_files(base_dir):
    """하위 폴더까지 모든 파일 경로와 파일명 추출 (.svn, .git 폴더 제외)"""
    all_files = []
    exclude_dirs = {".svn", ".git"}

    for root, dirs, files in os.walk(base_dir):
        # 제외할 폴더 제거
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            all_files.append({
                "path": file_path,
                "filename": file
            })
    return all_files


def save_to_csv(data, output_file="all_files.csv"):
    """결과를 CSV 파일로 저장"""
    if not data:
        print("저장할 데이터가 없습니다.")
        return

    fieldnames = ["path", "filename"]
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV 저장 완료: {output_file}")


if __name__ == "__main__":
    base_directory = r"C:\XMall4\svc\workspace\gnujava\src"  # 탐색 시작 경로 (원하는 폴더로 변경)
    results = scan_all_files(base_directory)

    # 결과 CSV 저장
    save_to_csv(results, "all_files.csv")
