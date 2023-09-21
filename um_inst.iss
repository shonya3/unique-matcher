[Setup]
AppName=Unique Matcher
AppVersion=0.3.0
DefaultDirName=UniqueMatcher
OutputBaseFilename=UniqueMatcherInstall
SetupIconFile=um.ico

[Files]
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs
Source: "dist\UniqueMatcher\*"; DestDir: "{app}"; Flags: recursesubdirs; Excludes: "dist\UniqueMatcher\PySide6\Qt6WebEngine*";
Source: "Tesseract-OCR\*"; DestDir: "{app}\Tesseract-OCR"; Flags: recursesubdirs

Source: "config.ini"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "screen.exe"; DestDir: "{app}"
Source: "README.md"; DestDir: "{app}"
Source: "LICENSE"; DestDir: "{app}"
Source: "um.ico"; DestDir: "{app}"

[Dirs]
Name: "{app}\data"
Name: "{app}\data\logs"
Name: "{app}\data\queue"
Name: "{app}\data\done"
Name: "{app}\data\errors"

[Tasks]
Name: desktopicon; Description: "Create a desktop icon"

[Icons]
Name: "{userdesktop}\Unique Matcher"; Filename: "{app}\UniqueMatcher.exe"; IconFilename: "{app}\um.ico"; Tasks: desktopicon
