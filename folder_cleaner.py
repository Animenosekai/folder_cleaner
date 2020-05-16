# IMPORTS
import tools.file_info as file_info
import tools.lifeeasy as lifeeasy

# GLOBAL VARIABLES DECLARATION
cleaning_dir = ''
destination_dir = ''
destination_dir_name = ''
unique_number = 1

# FUNCTIONS
def start():
    global cleaning_dir
    global destination_dir
    global destination_dir_name
    global unique_number
    lifeeasy.clear()
    print("What's the folder you want to clean today?")
    cleaning_dir = input('> ')
    if file_info.isdir(cleaning_dir):
        if cleaning_dir[-1] != '/' or cleaning_dir[-1] != '\\':
            if file_info.os_name == 'nt':
                cleaning_dir = cleaning_dir + '\\'
            else:
                cleaning_dir = cleaning_dir + '/'
        
        destination_dir_name = 'Cleaned'
        while file_info.exists(cleaning_dir + destination_dir_name):
            destination_dir_name = destination_dir_name + ' ' + str(unique_number)
            unique_number += 1
        destination_dir = cleaning_dir + destination_dir_name
        file_info.make_dir(destination_dir)
        decide_mode()
    else:
        lifeeasy.display_action('It seems like you mistyped the path', delay=0.1)
        print('Please retry entering the path to your folder')
        lifeeasy.sleep(2)
        start()

def decide_mode():
    lifeeasy.clear()
    print('Available options')
    print('')
    print('nosort   >   nothing will be sorted in your cleaned up folder')
    print('type     >   each file will be sorted and put in a folder according to its type')
    print('')
    print('')
    print('')
    print('How do you want to sort your cleaned folder?')
    decision = input('> ')
    if decision.lower() == 'cancel' or decision.lower() == 'stop' or decision.lower() == 'quit' or decision.lower() == 'exit':
        goodbye()
    elif decision.lower() == 'nosort' or decision.lower() == 'osort' or decision.lower() == 'nsort' or decision.lower() == 'noort' or decision.lower() == 'nosrt' or decision.lower() == 'nosot' or decision.lower() == 'nosor':
        lifeeasy.display_title('Cleaning your folder')
        lifeeasy.display_body(['Chosen mode: No Sorting'])
        lifeeasy.display()
        nosort()
    elif decision.lower() == 'type' or decision.lower() == 'ype'  or decision.lower() == 'tpe'  or decision.lower() == 'tye'  or decision.lower() == 'typ':
        lifeeasy.display_title('Cleaning your folder')
        lifeeasy.display_body(['Chosen mode: Type Sorting'])
        lifeeasy.display()
        sort_by_type()
    else:
        print('Sorry I did not understand.')
        lifeeasy.sleep(2)
        lifeeasy.clear()
        decide_mode()

def nosort():
    lifeeasy.display_body(['Chosen mode: No Sorting', 'Completion: 0%'])
    list_of_files_in_cleaning_dir = file_info.files_in_dir(cleaning_dir)
    lifeeasy.display_body(['Chosen mode: No Sorting', 'Completion: 1%'])
    completion = 0
    for file in list_of_files_in_cleaning_dir:
        completion += len(list_of_files_in_cleaning_dir) / 100 + 1
        lifeeasy.display_body(['Chosen mode: No Sorting', 'Completion: {}%'.format(completion)])
        if file == __file__:
            continue
        if file == destination_dir_name:
            continue
        file_info.move(cleaning_dir + file, destination_dir)
    lifeeasy.display_body(['Chosen mode: No Sorting', 'Completion: 100%'])
    goodbye()

def sort_by_type():
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 0%'])
    # _ are spaces
    # è are slashes (replaced by & for path compatibility)
    # Images_3D needs to be changed to 3D Images
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 1%'])

    Archives = []
    Audios = []
    Backups = []
    eBooks = []
    Database_Files = []
    Developers = []
    Disk_Images = []
    Encoded_Files = []
    ApplicationsèExecutables = []
    Fonts = []
    Images_3D = []
    Plugins = []
    PresetsèSettings = []
    Images = []
    Raw_Images = []
    ROMèGame_Files = []
    Spreadsheets = []
    System_Files = []
    Text_FilesèDocuments = []
    Vector_Images = []
    Videos = []
    Web_Documents = []
    Folders = []
    Other = []
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 2%'])

    list_of_files_in_cleaning_dir = file_info.files_in_dir(cleaning_dir)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 5%'])
    completion = 0
    for file in list_of_files_in_cleaning_dir:
        completion += len(list_of_files_in_cleaning_dir) / 75 + 5
        lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: {}%'.format(completion)])
        if file == __file__:
            continue
        if file == destination_dir_name:
            continue
        file_type = file_info.type_from_extension(file_info.extension_from_base(file))
        if file_type == 'Archive':
            Archives.append(file)
        elif file_type == 'Audio':
            Audios.append(file)
        elif file_type == 'Backup':
            Backups.append(file)
        elif file_type == 'eBook':
            eBooks.append(file)
        elif file_type == 'Database File':
            Database_Files.append(file)
        elif file_type == 'Developer':
            Developers.append(file)
        elif file_type == 'Disk Image':
            Disk_Images.append(file)
        elif file_type == 'Encoded File':
            Encoded_Files.append(file)
        elif file_type == 'Application/Executable':
            ApplicationsèExecutables.append(file)
        elif file_type == 'Font':
            Fonts.append(file)
        elif file_type == '3D Image':
            Images_3D.append(file)
        elif file_type == 'Plugin':
            Plugins.append(file)
        elif file_type == 'Preset/Settings':
            PresetsèSettings.append(file)
        elif file_type == 'Image':
            Images.append(file)
        elif file_type == 'Raw Image':
            Raw_Images.append(file)
        elif file_type == 'ROM/Game File':
            ROMèGame_Files.append(file)
        elif file_type == 'Spreadsheet':
            Spreadsheets.append(file)
        elif file_type == 'System File':
            System_Files.append(file)
        elif file_type == 'Text File/Document':
            Text_FilesèDocuments.append(file)
        elif file_type == 'Vector Image':
            Vector_Images.append(file)
        elif file_type == 'Video':
            Videos.append(file)
        elif file_type == 'Web Document':
            Web_Documents.append(file)
        elif file_type == 'Folder':
            Folders.append(file)
        elif file_type == 'Document':
            Text_FilesèDocuments.append(file)
        else:
            Other.append(file)

    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 76%'])
    if len(Archives) != 0:
        archives_path = file_info.make_dir(destination_dir + '/Archives')
        for file in Archives:
            file_info.move(cleaning_dir + file, archives_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 77%'])
    if len(Audios) != 0:
        Audios_path = file_info.make_dir(destination_dir + '/Audios')
        for file in Audios:
            file_info.move(cleaning_dir + file, Audios_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 78%'])
    if len(Backups) != 0:
        Backups_path = file_info.make_dir(destination_dir + '/Backups')
        for file in Backups:
            file_info.move(cleaning_dir + file, Backups_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 79%'])
    if len(eBooks) != 0:
        eBooks_path = file_info.make_dir(destination_dir + '/eBooks')
        for file in eBooks:
            file_info.move(cleaning_dir + file, eBooks_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 80%'])
    if len(Database_Files) != 0:
        Database_Files_path = file_info.make_dir(destination_dir + '/Database Files')
        for file in Database_Files:
            file_info.move(cleaning_dir + file, Database_Files_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 81%'])
    if len(Developers) != 0:
        Developers_path = file_info.make_dir(destination_dir + '/Developers')
        for file in Developers:
            file_info.move(cleaning_dir + file, Developers_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 82%'])
    if len(Disk_Images) != 0:
        Disk_Images_path = file_info.make_dir(destination_dir + '/Disk Images')
        for file in Disk_Images:
            file_info.move(cleaning_dir + file, Disk_Images_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 83%'])
    if len(Encoded_Files) != 0:
        Encoded_Files_path = file_info.make_dir(destination_dir + '/Encoded Files')
        for file in Encoded_Files:
            file_info.move(cleaning_dir + file, Encoded_Files_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 84%'])
    if len(ApplicationsèExecutables) != 0:
        ApplicationsèExecutables_path = file_info.make_dir(destination_dir + '/Applications & Executables')
        for file in ApplicationsèExecutables:
            file_info.move(cleaning_dir + file, ApplicationsèExecutables_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 85%'])
    if len(Fonts) != 0:
        Fonts_path = file_info.make_dir(destination_dir + '/Fonts')
        for file in Fonts:
            file_info.move(cleaning_dir + file, Fonts_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 86%'])
    if len(Images_3D) != 0:
        Images_3D_path = file_info.make_dir(destination_dir + '/3D Images')
        for file in Images_3D:
            file_info.move(cleaning_dir + file, Images_3D_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 87%'])
    if len(Plugins) != 0:
        Plugins_path = file_info.make_dir(destination_dir + '/Plugins')
        for file in Plugins:
            file_info.move(cleaning_dir + file, Plugins_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 88%'])
    if len(PresetsèSettings) != 0:
        PresetsèSettings_path = file_info.make_dir(destination_dir + '/Presets & Settings')
        for file in PresetsèSettings:
            file_info.move(cleaning_dir + file, PresetsèSettings_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 89%'])
    if len(Images) != 0:
        Images_path = file_info.make_dir(destination_dir + '/Images')
        for file in Images:
            file_info.move(cleaning_dir + file, Images_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 90%'])
    if len(Raw_Images) != 0:
        Raw_Images_path = file_info.make_dir(destination_dir + '/Raw Images')
        for file in Raw_Images:
            file_info.move(cleaning_dir + file, Raw_Images_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 91%'])
    if len(ROMèGame_Files) != 0:
        ROMèGame_Files_path = file_info.make_dir(destination_dir + '/ROM & Game Files')
        for file in ROMèGame_Files:
            file_info.move(cleaning_dir + file, ROMèGame_Files_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 92%'])
    if len(Spreadsheets) != 0:
        Spreadsheets_path = file_info.make_dir(destination_dir + '/Spreadsheets')
        for file in Spreadsheets:
            file_info.move(cleaning_dir + file, Spreadsheets_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 93%'])
    if len(System_Files) != 0:
        System_Files_path = file_info.make_dir(destination_dir + '/System Files')
        for file in System_Files:
            file_info.move(cleaning_dir + file, System_Files_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 94%'])
    if len(Text_FilesèDocuments) != 0:
        Text_FilesèDocuments_path = file_info.make_dir(destination_dir + '/Text Files & Documents')
        for file in Text_FilesèDocuments:
            file_info.move(cleaning_dir + file, Text_FilesèDocuments_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 95%'])
    if len(Vector_Images) != 0:
        Vector_Images_path = file_info.make_dir(destination_dir + '/Vector Images')
        for file in Vector_Images:
            file_info.move(cleaning_dir + file, Vector_Images_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 96%'])
    if len(Videos) != 0:
        Videos_path = file_info.make_dir(destination_dir + '/Videos')
        for file in Videos:
            file_info.move(cleaning_dir + file, Videos_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 97%'])
    if len(Web_Documents) != 0:
        Web_Documents_path = file_info.make_dir(destination_dir + '/Web Documents')
        for file in Web_Documents:
            file_info.move(cleaning_dir + file, Web_Documents_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 98%'])
    if len(Folders) != 0:
        Folders_path = file_info.make_dir(destination_dir + '/Folders')
        for file in Folders:
            file_info.move(cleaning_dir + file, Folders_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 99%'])
    if len(Other) != 0:
        Other_path = file_info.make_dir(destination_dir + '/Other')
        for file in Other:
            file_info.move(cleaning_dir + file, Other_path)
    lifeeasy.display_body(['Chosen mode: Type Sorting', 'Completion: 100%'])
    goodbye()


def goodbye():
    lifeeasy.stop_multi_thread_display()
    lifeeasy.display_action('Opening the folder', delay=0.1)
    file_info.open(cleaning_dir)
    lifeeasy.display_action('Opening your the result folder', delay=0.1)
    file_info.open(destination_dir)
    lifeeasy.clear()
    lifeeasy.display_title("Thank you for using this program")
    lifeeasy.display_body(['Folder Cleaner', '©Anime no Sekai - 2020', ''])
    lifeeasy.display()
    lifeeasy.stop_multi_thread_display()

start()