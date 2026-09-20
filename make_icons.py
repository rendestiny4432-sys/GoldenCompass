from pathlib import Path
from PIL import Image


# ==========================================
# 黄金の旅路コンパス
# PWAアイコン作成ツール
# ==========================================

folder = Path(__file__).parent

source_file = folder / "icon-original.png"

icon_192 = folder / "icon-192.png"
icon_512 = folder / "icon-512.png"


print()
print("🏇 黄金の旅路コンパス")
print("PWAアイコンを作成します。")
print()


# ==========================================
# 元画像確認
# ==========================================

if not source_file.exists():

    print("❌ icon-original.png が見つかりません。")
    print()

    input("Enterキーで終了します。")

    raise SystemExit


# ==========================================
# 画像読み込み
# ==========================================

print("🎨 元画像を読み込み中...")

image = Image.open(source_file)

image = image.convert("RGBA")


# ==========================================
# 192 x 192
# ==========================================

print("📱 icon-192.png を作成中...")

small_icon = image.resize(
    (192, 192),
    Image.Resampling.LANCZOS
)

small_icon.save(
    icon_192,
    "PNG"
)


# ==========================================
# 512 x 512
# ==========================================

print("📱 icon-512.png を作成中...")

large_icon = image.resize(
    (512, 512),
    Image.Resampling.LANCZOS
)

large_icon.save(
    icon_512,
    "PNG"
)


# ==========================================
# 完了
# ==========================================

print()
print("✨ 完成！！")
print()
print("作成したアイコン：")
print("  icon-192.png")
print("  icon-512.png")
print()
print(
    "アネゴ「よし！ "
    "旅の目印もできたな、アナタ！」"
)
print()