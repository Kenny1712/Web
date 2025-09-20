import PyBypass as bypasser

def bypass_link(url: str, name: str = None) -> str:
    """
    Bypass link và trả về link gốc (hoặc link đích cuối cùng).
    name: chỉ định rõ nếu domain phức tạp (vd: "linkvertise")
    """
    try:
        if name:
            result = bypasser.bypass(url, name=name)
        else:
            result = bypasser.bypass(url)
        return result
    except Exception as e:
        print("Lỗi khi bypass:", e)
        return None

if __name__ == "__main__":
    # Ví dụ:
    for url in [
        "https://link4m.com/go/gv0NrbY"
    ]:
        final = bypass_link(url, name="linkvertise")
        print(url, "→", final)
