import subprocess

def run_scripts():
    try:
        # 첫 번째 프로그램 실행
        print(">>> getMonthETF.py 실행 중...")
        subprocess.run(["python", "getMonthETF.py"], check=True)

        # 두 번째 프로그램 실행
        print(">>> updateData.py 실행 중...")
        subprocess.run(["python", "updateData.py"], check=True)

        print(">>> 모든 프로그램 실행 완료!")

    except subprocess.CalledProcessError as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    run_scripts()
