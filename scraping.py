import os
import json
import pandas as pd
from bs4 import BeautifulSoup

print(" STARTING TEXT FILE PROCESSING")

final_products = []

#ALl txt files which created from website 
txt_files = [
    'ACCESSORIES.txt', 'ADAPTERS.txt', 'AIR_PODS.txt', 'EARBUDS.txt', 
    'GADGET.txt', 'LAPTOP_LIST.txt', 'MAC_BOOK_CASES.txt', 'MOBILE_LIST.txt', 
    'OVER_EAR_HEADPHN.txt', 'PHONE_CASES.txt', 'POWER_BANK.txt', 
    'SCREEN_PROTECTOR.txt', 'SMART_WATCH.txt', 'SOUNDS.txt', 'TABLET_LIST.txt'
]

if not txt_files:
    print("NO TEXT FILE FIND.PLEASE KEEP ALL FILE IN FOLDER")
else:
    for file_path in txt_files:
        print(f"⏳ '{file_path}' File is processing ")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                raw_json = json.load(file)
                
            # Looping all product
            for product in raw_json.get('data', []):
                
                # clinning HTML description
                html_desc = product.get('description', '')
                clean_desc = BeautifulSoup(html_desc, 'html.parser').get_text(separator=" ").strip() if html_desc else ""
                
                # Extracting Price
                price_info = product.get('price', {}) or {}
                current_price = price_info.get('price', 'N/A')
                original_price = price_info.get('compare_price', 'N/A')
                
                # Checking duplicate data
                p_name = product.get('name')
                if p_name not in [p['Product Name'] for p in final_products]:
                    final_products.append({
                        "Product Name": p_name,
                        "Current Price": current_price,
                        "Original Price": original_price,
                        "Thumbnail URL": product.get('thumbnail'),
                        "Product Description": clean_desc
                    })
                    
        except Exception as e:
            print(f"⚠️ '{file_path}' ERROR CREATED {str(e)}")

    # ৩. Combined all data in one csv
    if final_products:
        df = pd.DataFrame(final_products)
        df.to_csv("dazzle_master_dataset.csv", index=False, encoding='utf-8-sig')
        print(f"\nDONE FROM ALL FILE {len(df)} THIS UNIQUE DATA CREATED  'dazzle_master_dataset.csv' ")
    else:
        print("FAILD TO CREATE")