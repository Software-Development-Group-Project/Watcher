import os
cwd = os.getcwd()


def relocate_rename_images(folder_path, new_folder_path, imageNum):    

    test_folders = os.listdir(folder_path)

    for folder in test_folders:
        
        img_folder_path = os.path.join(cwd, folder)    
        imgs = os.listdir(img_folder_path)

        num = imageNum
        
        for img in imgs:
            
            img_path = os.path.join(img_folder_path, img)
            new_img_path = os.path.join(new_folder_path, folder+"//"+folder+"."+str(num)+".jpg")            
            
            with open(img, "rb") as read_img:
                with open(new_img, "wb") as write_img:
                    for bytes_img in read_img:
                        write_img.write(bytes_img)
                        
            num += 1


folder_path = os.path.join(cwd, "dataset\\testing") 
new_folder_path = os.path.join(cwd, "dataset\\training") 
relocate_rename_images(folder_path, new_folder_path)