import requests
import os
assetNames = ["skills",
              "library",
              "enemy",
              "npc",
              "pet",
              "mission",
              "gamedata",
              "talents",
              "skill-effect",
              "weapon-effect",
              "back_item-effect",
              "accessory-effect",
              "arena-effect"]
base_url = 'https://ns-assets.ninjasage.id/static/lib/'
save_dir = './download/assets'
os.makedirs (save_dir, exist_ok=True)

for asset in assetNames:
    file_url = f"{base_url}{asset}.bin"

    response = requests.get(file_url)

    if response.status_code == 200:
        file_path = os.path.join(save_dir, f'{asset}.bin')

        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded {asset}")
    
    else:
        print(f'Failed to download {asset}')

print('Download complete')

