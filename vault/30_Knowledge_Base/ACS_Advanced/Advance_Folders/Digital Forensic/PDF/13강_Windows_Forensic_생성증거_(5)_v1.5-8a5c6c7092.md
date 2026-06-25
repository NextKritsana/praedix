---
title: "13강_Windows_Forensic_생성증거_(5)_v1.5"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\13강_Windows_Forensic_생성증거_(5)_v1.5.pdf"
source_size_bytes: 921590
source_modified: 2025-10-11T21:46:24
imported_at: 2026-06-14T14:25:03
tags:
  - acs
  - acs-advanced
  - imported
---

# 13강_Windows_Forensic_생성증거_(5)_v1.5

- Source: [13강_Windows_Forensic_생성증거_(5)_v1.5.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/13%EA%B0%95_Windows_Forensic_%EC%83%9D%EC%84%B1%EC%A6%9D%EA%B1%B0_%285%29_v1.5.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Windows Forensic – 생성
증거 (5)
• 링크 파일 이란
• 링크 파일의 구조
• 링크 파일 분석 도구
• 링크 파일 분석
• 링크 파일 분석의 한계
13
1

## Page 2

링크 파일 이란01
디지털 포렌식의 세계에서 상대적으로 소소해 보일 수 있지만,
사실은 사용자의 행동과 시스템 상호작용의 중요한 단서를 제공하는 놀라운 자원
바로 링크 파일(.lnk)에 대해 알아보는 시간을 갖을 예정
바탕화면이나 문서 폴더에서 보게 되는 이 작은 아이콘들이 어떻게 범죄 수사, 보안 침해 조사,
심지어는 일상적인 시스템 모니터링에서 귀중한 정보의 보물창고가 될 수 있는지를 탐구함
링크 파일 하나하나가 담고 있는 이야기를 해독하는 방법을 배움으로써,
디지털 포렌식 전문가로서의 능력 한층 더 향상 시킬 수 있음
2

## Page 3

링크 파일 이란01
Link File 01
03
02
04
역사
Microsoft Windows의
바로 가기 파일 형식
Windows 95와 함께 처음 도입
목적
사용자에게 편의성을 제공하는 것
자주 사용하는 프로그램이나 파일, 디렉토리에 대
한 바로 가기를 생성함으로써, 사용자는 더욱 빠르
고 게 해당 자원에 접근할 수 있게 됨
개념 및 정의
특정 파일이나 디렉토리, 또는 네트워크 자원
에 대한 참조를 담고 있는 바로 가기 파일
장점: 빠른 접근성과 편의성 제공
사용자가 필요한 자원을 직접 찾아가지 않고도
lnk 파일을 통해 쉽게 접근 가능
단점: 보안 문제. 악성 코드를 숨기거나, 사용자의 활
동 추적에 이용 가능
3

## Page 4

링크 파일 이란01
Link File 01
03
02
필요성
사용자의 컴퓨터 사용 경험을 크게 향상시켜주는 도구
특히 대용량의 데이터를 다루는 현대의 컴퓨터 환경에서,
원하는 자원을 빠르게 찾아 접근하는 것은 매우 중요한 일
이러한 측면에서 .lnk 파일의 필요성은 매우 큼
디지털 포렌식 관점
사용자가 어떤 파일을 언제 열었는지,
어떤 프로그램을 언제 실행했는지 등의 정보를 포함
하고 있기 때문
사용되는 과정
원본 자원에 대한 참조 정보를 담고 있음
이 파일을 실행하면, 운영체제는 이 참조 정보를 읽어
해당 자원을 로드하거나 실행함
사용자 활동 추적: LNK 파일은 사용자가 어떤 파일을 열었는지, 어떤 프로그램을 실행했는지 등의 정보를 포함함 이를 통해
디지털 포렌식 전문가는 사용자의 활동을 추적하고, 의심스러운 행동을 찾아 낼 수 있음
파일 삭제 추적: 사용자가 파일을 삭제하더라도, 해당 파일에 대한 LNK 파일이 남아 있을 수 있음 이를 통해 디지털 포렌식 전
문가는 삭제된 파일에 대한 정보 획득 가능
네트워크 활동 추적: LNK 파일은 네트워크 자원에 대한 참조 정보도 포함하고 있습니다. 이를 통해 디지털 포렌식 전문가는
사용자가 어떤 네트워크 자원에 접근했는지를 추적 가능
악성 코드 분석: 악성 코드는 종종 LNK 파일을 이용하여 시스템에 침투하거나, 시스템 내에서 활동합니다. 디지털 포렌식 전
문가는 이 LNK 파일을 분석하여 악성 코드의 행동을 이해하고, 침투 경로를 찾아낼 수 있습니다.
 4

## Page 5

링크 파일의 구조02
Link File
Open Chrome
Through 010editor
Chrome LNK FIle Chrome EXE FIle
Chrome.exe
유형: 실행 가능 파일 (Executable File)
목적: Google Chrome 웹 브라우저의 주 실행 파일
이 파일을 실행하면 Google Chrome 브라우저가 시작.
구조: .exe 형식의 파일은 컴파일된 바이너리 코드를 포함하고 있음
운영 체제에서 직접 실행할 수 있는 명령어와 데이터를 포함
파일 내부에는 프로그램의 로직, 자원, 종속성 정보 등이 포함
Windows에서는 PE (Portable Executable) 형식을 따름
분석 시: 바이너리 분석 도구나 디컴파일러를 사용하여 파일 내부의
코드와 리소스를 검토할 수 있음
이를 통해 프로그램의 구조, 사용된 프로그래밍 기법,
외부 라이브러리 호출 등을 확인 가능
Chrome.lnk
유형: 바로 가기 (Shortcut) 파일
구조: .lnk 파일은 Windows의 바로 가기를 정의하는 구조를
가지고 있으며, 대상 경로, 시작 폴더, 창 상태, 아이콘 위치 등
실행에 필요한 다양한 속성 정보 포함 이 파일 내부 구조는
복잡한 바이너리 형식으로 되어 있으며,
LNK 파일 형식의 사양에 따름
분석 시: 바로 가기 파일의 속성과 설정을 검토할 수 있는 도구를
사용하여 파일이 가리키는 대상, 추가 매개변수, 아이콘 정보 등을
확인할 수 있음 보안 분야에서는 때때로 .lnk 파일이 악성 코드의
전달 메커니즘으로 사용될 수 있기 때문에,
이러한 파일을 분석하여 보안 위협을 탐지하기도 함
5

## Page 6

링크 파일의 구조02
.lnk Structure
ShellLinkHeader
LinkTargetIDList
LinkInfo
StringsData
ExtraData
ShellLinkHeader: 링크 파일의 기본 정보를 담고 있음
이 섹션은 필수적으로 존재하며,
링크 파일의 크기, 생성 시간, 대상 파일의 특성 등의 정보 저장
LinkTargetIDList: 선택적으로 포함될 수 있으며,
링크 대상의 상세 정보를 담고 있음
ShellLinkHeader의 HasLinkTargetIDList 플래그가 설정되어 있을 때만 존재
링크 대상의 전체 경로, 파일 시스템 위치, 네트워크 위치 등의 정보 포함
LinkInfo: 선택적으로 포함될 수 있으며, 링크 대상의 위치 정보를 제공
ShellLinkHeader의 HasLinkInfo 플래그가 설정되어 있을 때만 존재
 링크 대상의 상대 경로나, 볼륨 정보, 네트워크 공유 정보 등을 포함
StringData: 링크 대상의 문자열 정보를 포함
ShellLinkHeader의 다양한 플래그가 설정되어 있을 때만 존재
대상 파일의 이름, 작업 디렉터리, 설명, 상대 경로 등의 문자열 정보
ExtraData: 추가적인 정보를 저장
선택적으로 포함될 수 있으며, 화면 표시 정보, 문자열 코드 페이지 정보,
환경 변수 정보 등을 포함
6

## Page 7

링크 파일의 구조02
ShellLinkHeader
HeaderSize LinkCLSID
LinkFlags FileAttributes CreationTime
AccessTime WirteTime
FileSize IconIndex ShowCommand
HotKey Reserved1 Reserved2 Reserved3
HeaderSize – 헤더의 크기로 항상 0x0000004C의 값으로 고정
LinkCLSID – 클래스 식별자 Class Identifier 로
항상  00021401 – 0000 – 0000 – 0000000000046
LinkFlags – 링크 대상의 다양한 정보에 대한 플래그 값
LinkFlags 필드는 ShellLinkHeader의 특정 부분을 참조하는
여러 비트 플래그 포함
이 중에서 HasLinkTargetIDList 플래그는 LinkTargetIDList
구조가 .lnk 파일에 포함되어 있는지를 나타내는 플래그
HasLinkTargetIDList 플래그는 LinkFlags의 가장 하위 비트에
위치하며, 이 플래그가 1로 설정되어 있으면 LinkTargetIDList 구조가
.lnk 파일에 포함되어 있음을 의미
그 반대의 경우, 즉 이 플래그가 0으로 설정되어 있으면
LinkTargetIDList 구조가.lnk 에 포함되어 있지 않음을 의미
HasLinkInfo 플래그는 LinkInfo 구조가 .lnk 파일에 포함되어
있는지를 나타내는 플래그
HasLinkInfo 플래그는 LinkFlags의 두 번째 비트에 위치
이 플래그가 1로 설정되어 있으면
LinkInfo 구조가 .lnk 파일에 포함되어 있음을 의미
그 반대의 경우, 즉 이 플래그가 0으로 설정되어 있으면 LinkInfo 구조
가 .lnk 파일에 포함되어 있지 않음을 의미
FileAttributes - 링크 대상의 파일의 특성 정보
7

## Page 8

링크 파일의 구조02
ShellLinkHeader
HeaderSize LinkCLSID
LinkFlags FileAttributes CreationTime
AccessTime WirteTime
FileSize IconIndex ShowCommand
HotKey Reserved1 Reserved2 Reserved3
CreationTime – 링크 대상의 생성시간
AccessTime – 링크 대상의 접근시간
WriteTime- 링크 대상의 쓰기시간
FileSize – 링크 대상의 크기
IconIndex – 아이콘 인덱스
ShowCommand – 링크가 실행될 때 응용프로그램의 동작 모드
 0x1 SW_NORMAL
 0x2 SW_SHOWMINIMIZED
 0x3 SW_SHOWMAXM
HotKey - Hotkey에 대한 정보
바로가기 파일(.lnk 파일)을 실행할 때 사용할 단축키를 지정하는 필드
Hotkey 필드는 2바이트로 구성되며,
이는 키보드의 단축키 조합을 나타냄
예를 들어, 'Ctrl + A'를 단축키로 설정하면
해당 바로가기 파일은 'Ctrl + A' 키를 눌렀을 때 실행
이 Hotkey 필드를 통해 사용자는 자주 사용하는 프로그램이나
파일에 대해 키보드 단축키를 설정할 수 있어,
더욱 빠르고 간편하게 해당 자원에 접근 가능
Reserved1,2,3 예약된 영역
8

## Page 9

LinkTargetIDList
링크 파일의 구조02
LinkTargetIDLIST란
LinkTargetIDList는 .lnk 파일, 즉 Windows 바로 가기
파일 내에서 링크 대상의 위치와 관련 정보를 식별하는
데 사용되는 중요한 구조
ShellLinkHeader의 HasLinkTargetIDList 플래그가
설정되어 있을 때만 포함되며,
링크 대상의 식별자 리스트(IDList)를 담고 있음
HasLinkTargetIDList 플래그
.lnk 파일의 LinkFlags 필드에는 여러 플래그가 있으며,
HasLinkTargetIDList는 이 중 하나입니다.
LinkFlags 필드의 가장 하위 비트에 위치하며,
이 비트가 1로 설정되어 있으면
LinkTargetIDList 구조가 파일에 존재함을 나타냄
9

## Page 10

LinkTargetIDList
링크 파일의 구조02
IDList Size
LinkTargetIDList의 첫 부분에는 IDList Size 필드가 있으며,
이는 바로 뒤에 오는 IDList의 크기를 바이트 단위로 나타냄
이 크기 정보는 IDList를 올바르게 파싱하는 데 필요
IDList
실제로 링크 대상에 대한 참조 정보를 담고 있는 항목들의 집합
여러 ItemID로 구성되며, 각 ItemID는 두 부분으로 나뉨
ItemID Size: 각 ItemID의 크기를 바이트 단위로 나타내며,
ItemID 데이터의 길이를 알려줌
ItemID: 실제 항목 식별자 데이터를 포함하며,
대상 파일, 폴더, 네트워크 자원 등을 나타냄
각 ItemID는 대상의 위치, 이름, 아이콘 등의 정보를
포함할 수 있으며, 각각의 ItemID 크기는 다를 수 도 있음
10

## Page 11

LinkTargetIDList
링크 파일의 구조02
작동 원리
사용자가 바로 가기를 클릭할 때,
Windows는 LinkTargetIDList를 사용하여 대상의 위치를 결
정
IDList 내의 ItemID들을 순차적으로 해석하면서
대상의 실제 경로를 구성
이 과정을 통해 파일 시스템 내에서 바로 가기가 가리키는
실제 객체에 접근 가능
디지털 포렌식 관점
LinkTargetIDList는 바로 가기 파일이 가리키는
대상의 구체적인 위치와 정보를 제공하는 핵심적인 역할
디지털 포렌식이나 보안 분석에서는 이 정보를 사용하여
사용자의 활동이나 바로 가기가 생성된 배경을
추적하고 분석이 가능
11

## Page 12

링크 파일의 구조02
LinkInfo
LinkInfo란
LinkInfo 구조는 바로 가기 대상의 실제 위치 정보를
저장하는 데 사용되며,
LinkTargetIDList와 함께 링크 대상을 찾는 데
필요한 중요한 정보를 제공
바로 가기가 가리키는 대상의 파일 시스템 위치를 설명
로컬 및 네트워크 파일 시스템에 대한
참조를 포함
12

## Page 13

링크 파일의 구조02
LinkInfo
LinkInfo 구조의 주요 요소
LinkInfo Size: LinkInfo 구조체의 전체 크기를 바이트 단위로 나타냄
이는 LinkInfo 구조의 끝을 식별하는 데 사용
LinkInfo Header Size: LinkInfo의 헤더 부분의 크기를 나타냄
헤더는 LinkInfo 구조의 나머지 부분을 해석하는 데 필요한 정보를 제공
LinkInfo Flags: LinkInfo에 대한 플래그를 포함하며,
이는 LinkInfo가 로컬 경로, 네트워크 경로 또는 둘 다를 포함하는지
여부와 같은 정보를 나타냄
VolumeID, LocalBasePath: 로컬 파일 시스템에 대한
링크 대상의 정보를 포함함
VolumeID는 링크 대상이 위치한 볼륨의 정보를
LocalBasePath는 해당 볼륨 내에서 대상의 절대 경로를 제공
CommonNetworkRelativeLink: 네트워크 리소스에 대한
링크 대상의 정보를 포함
네트워크 공유의 이름과 네트워크 경로 등을 나타냄
CommonPathSuffix: 로컬 및 네트워크 경로 모두에
공통적으로 적용되는 대상 경로의 나머지 부분을 나타냄
13

## Page 14

링크 파일의 구조02
LinkInfo
작동 원리
LinkInfo 구조는 바로 가기가 로컬 파일 시스템이나 네트워크 위치를
가리키는 경우에 해당 정보를 정확하게 나타내기 위해 사용
사용자가 바로 가기를 클릭하면, Windows는 LinkInfo에 저장된 정보를
사용하여 대상의 실제 위치를 결정하고 접근
로컬 파일 시스템에 대한 링크의 경우, VolumeID와 LocalBasePath를
사용하여 대상 파일이나 폴더에 접근
네트워크 리소스의 경우, CommonNetworkRelativeLink 정보를
사용하여 네트워크 경로를 해석하고 연결
중요성
LinkInfo는 .lnk 파일이 가리키는 대상의 위치를 정확하게 찾아내는 데
필수적인 정보를 제공
사용자가 시스템 내외부의 다양한 리소스에 대한 빠른 접근을 만듬
디지털 포렌식 및 보안 분석에서 LinkInfo는 사용자의 활동 추적,
파일 접근 패턴 분석, 악성 소프트웨어의 활동 감지 등에
사용될 수 있는 중요한 정보를 제공
.lnk 파일의 LinkInfo 구조를 이해하는 것은 바로 가기 파일의 작동 방식과
대상 위치 식별 방법을 파악하는 데 중요하며,
파일 시스템과 네트워크 자원에 대한 접근 방식을 이해하는 데 도움됨
14

## Page 15

링크 파일의 구조02
StringsData
 StringData 란
StringData 섹션은 바로 가기 대상과 관련된
추가적인 문자열 정보를 제공하는 중요한 부분
바로 가기의 기능성과 사용자 인터페이스에
필요한 정보를 담고 있으며,
ShellLinkHeader의 특정 플래그들이
설정되어 있을 때만 포함
StringData 구조의 주요 요소
•CountCharacters: 각 문자열 데이터 블록의
시작 부분에 위치하며, 바로 다음에 오는 문자열의
길이(문자 단위)를 나타냄
이 값은 null 종료 문자를 포함하지 않음
•String: CountCharacters에 의해 지정된 길이를
가진 실제 유니코드 문자열
이 문자열은 .lnk 파일이 가리키는 대상에 대한
다양한 정보를 제공
15

## Page 16

링크 파일의 구조02
StringsData
StringData가 포함할 수 있는 정보
NameString (링크 대상의 이름): 사용자에게 보여지는 링크의 이름
으로, 일반적으로 대상 파일이나 폴더의 이름을 나타냄
RelativePath : 바로 가기 대상까지의 상대적인 파일 경로
바로 가기 파일이 위치한 곳으로부터 대상까지의 경로를 기술
WorkingDir (작업 디렉터리): 바로 가기를 통해 실행될 때
사용되는 기본 작업 디렉터리의 경로
프로그램이나 스크립트를 실행할 때
필요한 작업 환경을 설정하는 데 사용
IconLocation (아이콘 위치): 바로 가기에 사용되는 아이콘의 파일
경로와, 해당 파일 내에서 아이콘의 인덱스를 나타냄
사용자는 바로 가기의 시각적 식별을 위한 커스텀 아이콘을 설정
중요성 및 용도
StringData 섹션은 .lnk 파일이 사용자에게 제공하는 정보의 범위와
세부사항을 향상시키며, 사용자 경험을 개선하는 데 중요한 역할
예를 들어, NameString은 사용자가 바로 가기를 식별하는 데 도움을
주고, WorkingDir은 프로그램이 올바르게 실행될 수 있도록 환경을
설정하는 데 필수적
IconLocation은 사용자 인터페이스의 시각적 요소를 개선하여,
바로 가기를 더 쉽게 인식할 수 있게 함
.lnk 파일의 StringData 섹션을 통해, 개발자와 사용자는 바로 가기
를 통해 보다 풍부하고 유용한 정보를 제공하고 받을 수 있으며,
이는 사용자의 파일 관리 및 접근성을 향상시키는 데 기여
16

## Page 17

링크 파일의 구조02
ExtraData
ExtraData란
ExtraData 구조는 바로 가기 파일에 추가적인 세부 정보를 저장하는
데 사용되며,
이는 .lnk 파일의 기능성을 확장하고 사용자 경험을 풍부하게 함
ExtraData는 선택적으로 포함되며,
다양한 데이터 블록을 포함할 수 있음
각각의 데이터 블록은 바로 가기의 특정 측면이나 사용 환경에 대한 정
보를 제공함
각 데이터 블록의 구조
BlockSize: 데이터 블록의 전체 크기를 나타내는 필드
이 크기는 데이터 블록의 모든 부분,
즉 헤더와 데이터를 포함한 총 크기를 바이트 단위로 나타냄
BlockSignature: 데이터 블록의 타입을 식별하는 고유한 시그니처
이 시그니처는 각 데이터 블록의 유형을 구분하는 데 사용
BlockData: 실제 데이터를 포함하는 섹션으로,
BlockSignature에 정의된 형식에 따라 데이터가 저장됨
17

## Page 18

링크 파일의 구조02
ExtraData
ExtraData 섹션에 포함될 수 있는 다양한 타입의 데이터 블록
ConsoleDataBlock: 콘솔 창(명령 프롬프트)의 설정 정보를 저장
이는 창 크기, 버퍼 크기, 텍스트 및 배경 색상 등을 포함
ConsoleFEDataBlock: 콘솔 창의 글꼴 정보,
특히 동아시아 언어를 위한 글꼴 정보를 포함
DarwinDataBlock: Windows Installer를 통해 설치된 애플리케이션의 식별자를
포함 이는 MSI 패키지의 정보를 참조하는 데 사용
EnvironmentVariableDataBlock: 바로 가기가 실행될 때 참조할 수 있는
환경 변수에 대한 정보를 포함
IconEnvironmentDataBlock: 바로 가기의 아이콘 위치 정보를 포함하며,
아이콘 파일의 경로와 인덱스를 저장
KnownFolderDataBlock: 사용자의 알려진 폴더
(예: 문서, 이미지, 다운로드 폴더 등)에 대한 참조를 포함
PropertyStoreDataBlock: 파일에 대한 속성 정보를 포함하며,
이는 메타데이터나 사용자 정의 속성을 저장하는 데 사용
ShimDataBlock: 애플리케이션 호환성 층(Shims) 설정 정보를 포함
이는 호환성 문제를 해결하기 위해 특정 옵션을 적용하는 데 사용
SpecialFolderDataBlock: 특수 폴더의 ID를 포함하며,
이는 바로 가기가 가리키는 특정 시스템 폴더의 위치를 나타냄
TrackerDataBlock: 링크 대상의 분산 링크 추적 정보를 포함
이는 바로 가기가 가리키는 파일이 이동되거나 이름이 변경되었을 때도
올바른 파일을 찾는 데 사용
VistaAndAboveIDListDataBlock: Windows Vista 이상의 운영체제에서 사용하
는 IDList를 포함 이는 바로 가기가 가리키는 대상의 IDList를 최신 운영체제에서
사용할 수 있도록 저장
18

## Page 19

링크 파일의 구조02
출처 : [MS-SHLLINK]: Shell Link (.LNK) Binary File Format | Microsoft Learn
19

## Page 20

링크 파일 분석  도구03
Made by Eric Zimmerman
Https://github.com/EricZimmerman/LECmd
.\LECmd.exe -f “path to lnk file＂
–csv “[csv파일을 저장하고 싶은 곳”
LECmd
실행화면
20

## Page 21

링크 파일 분석  도구03
실행화면
SourceFile: 이는 분석 대상인 LNK 파일의 전체 경로를 나타냄
LNK 파일의 위치를 정확히 나타내므로, 파일의 원래 위치를 알 수 있음
SourceCreated: LNK 파일이 생성된 날짜와 시간을 나타냄
이 정보는 파일이 처음 생성된 시점을 알려주고, 이는 사용자의 특정 활동이나
이벤트와 연관 지을 수 있음
SourceModified: LNK 파일이 마지막으로 수정된 날짜와 시간을 나타냄
이 정보는 파일의 속성이나 내용이 변경된 최근 시점을 알려주며,
이는 파일의 업데이트 상태를 파악하는데 도움이 됨
SourceAccessed: LNK 파일에 마지막으로 접근한 날짜와 시간을 나타냄
이는 파일을 열거나, 파일의 속성을 확인한 최근 시점을 알려주며,
이는 파일의 사용 패턴을 파악하는데 도움이 됨
TargetCreated: LNK 파일이 가리키는 대상 파일이 생성된 날짜와 시간을 나타냄
이 정보는 대상 파일이 처음 생성된 시점을 알려주고,
이는 대상 파일의 생성 이력을 파악하는데 도움이 됨
TargetModified: LNK 파일이 가리키는 대상 파일이 마지막으로 수정된 날짜와
시간을 나타냄
이 정보는 대상 파일의 속성이나 내용이 변경된 최근 시점을 알려주며,
이는 대상 파일의 업데이트 상태를 파악하는데 도움이 됨
TargetAccessed: LNK 파일이 가리키는 대상 파일에 마지막으로 접근한 날짜와
시간을 나타냄
이는 대상 파일을 열거나, 대상 파일의 속성을 확인한 최근 시점을 알려주며,
이는 대상 파일의 사용 패턴을 파악하는데 도움이 됨
LECmd로 생성한 CSV파일
21

## Page 22

링크 파일 분석  도구03
실행화면
FileSize: LNK 파일이 가리키는 대상 파일의 크기를 바이트 단위로 나타냄
이 정보는 대상 파일의 크기를 알려주며,
이는 파일의 용량을 파악하는데 도움이 됨
RelativePath: 이는 LNK 파일이 가리키는 대상 파일의 상대 경로를 나타냄
상대 경로는 LNK 파일의 위치에 대한 대상 파일의 위치를 나타내므로,
대상 파일의 위치를 파악하는데 도움이 됩니다.
WorkingDirectory:  LNK 파일이 가리키는 대상 파일의 작업 디렉토리를 나타냄
작업 디렉토리는 프로그램이 실행되는 동안 파일을 찾는 기본 디렉토리 의미
FileAttributes: LNK 파일이 가리키는 대상 파일의 파일 속성을 나타냄
파일 속성에는 읽기 전용, 숨김, 시스템, 아카이브 등이 포함됨
HeaderFlags: 이는 LNK 파일의 헤더 플래그를 나타냄
헤더 플래그는 LNK 파일의 다양한 설정과 상태를 나타내는 비트 필드
DriveType: LNK 파일이 가리키는 대상 파일이 위치한 드라이브의 타입을 나타냄
드라이브 타입에는 하드 디스크, 네트워크 드라이브, CD-ROM 드라이브
등이 있을 수 있음
VolumeSerialNumber: LNK 파일이 가리키는 대상 파일이 위치한 볼륨의
시리얼 번호를 나타냄
볼륨 시리얼 번호는 파일 시스템을 식별하는 데 사용되는 고유한 번호
VolumeLabel: LNK가 가리키는 대상 파일이 위치한 볼륨의 레이블을 나타냄
볼륨 레이블은 볼륨을 설명하는 텍스트 라벨
LECmd로 생성한 CSV파일
22

## Page 23

링크 파일 분석  도구03
LECmd로 생성한 CSV파일
실행화면
LocalPath: 이는 LNK 파일이 가리키는 대상 파일의 로컬 경로를 나타냄
로컬 경로는 로컬 파일 시스템 내에서 대상 파일의 위치를 나타냄
NetworkPath: 이는 LNK 파일이 가리키는 대상 파일의 네트워크 경로를 나타냄
네트워크 경로는 네트워크를 통해 대상 파일에 접근하는 데 사용되는 경로
CommonPath: 이는 LNK 파일이 가리키는 대상 파일의 공통 경로를 나타냄
공통 경로는 대상 파일의 경로 중 LNK 파일의 경로와 공통된 부분을 나타냄
이는 LNK 파일과 대상 파일의 상대적인 위치를 파악하는 데 도움이 됨
Arguments: 이는 LNK 파일이 가리키는 대상 파일을 실행할 때 사용되는 인수
이 인수는 프로그램이 실행될 때 전달되는 추가 정보로,
프로그램의 동작을 제어하는데 사용
TargetIDAbsolitePath: LNK 파일이 가리키는 대상 파일의 절대 경로를 나타냄
절대 경로는 루트 디렉토리부터 시작하는 파일의 전체 경로
TargetMFTEntryNumber: LNK 파일이 가리키는 대상 파일의 MFT(Master File
Table) 엔트리 번호를 나타냄
MFT 엔트리 번호 : 파일 시스템 내에서 파일을 식별하는 데 사용되는 고유한 번호
TargetMFTSequenceNumber: 이는 LNK 파일이 가리키는 대상 파일의 MFT 엔
트리 시퀀스 번호를 나타냄
MFT 엔트리 시퀀스 번호는 MFT 엔트리가 재사용될 때마다 증가하는 번호
23

## Page 24

링크 파일 분석  도구03
LECmd로 생성한 CSV파일
실행화면
MachineID: 이는 LNK 파일을 생성한 기기의 ID를 나타냄
기기 ID는 컴퓨터를 식별하는 데 사용되는 고유한 식별자
MachineMACAddress: 이는 LNK 파일을 생성한 기기의 MAC 주소를 나타냄
MAC 주소는 네트워크 인터페이스를 식별하는 데 사용되는 고유한 주소
MACVendor: 이는 LNK 파일을 생성한 기기의 MAC 주소 벤더를 나타냄
MAC 주소 벤더는 MAC 주소의 처음 6자리를 통해 식별되며,
네트워크 인터페이스 카드를 제조한 회사를 나타냄
TrackerCreatedOn: 이는 LNK 파일의 트래커가 생성된 날짜를 나타냄
트래커는 파일의 변경 이력을 추적하는 데 사용되는 정보
ExtraBlocksPresent: 이는 LNK 파일에 포함된 추가 데이터 블록들의 정보
추가 데이터 블록 LNK 파일의 기본 정보 외에 추가적인 정보를 저장하는 데 사용
이 정보는 LNK 파일의 생성 환경, 네트워크 정보 등 다양한 정보를 포함
24

## Page 25

TEXT ADD
Smooth like butter Like a criminal undercover Gon' pop like trouble Breakin' into your heart Breakin' into your heart like that
TEXT ADD
Smooth like butter Like a criminal undercover Gon' pop like trouble Breakin' into your heart Breakin' into your heart like that
링크 파일 분석04
먼저 분석 대상으로 Chrome.lnk 파일을 대상으로 진행하였으며 내 PC의 C드라이브의 데스크탑에 SJM이라는 폴더에 포함됨
SourceFile는 말 그대로 소스로 사용된 파일 위에서 말한것 처럼 내 pc의 데스크탑의 SJM폴더내의 Chrome.lnk파일을 대상으로 분석했음을 보여줌
생성시간은 분석진행을 위해 이전에 바탕화면에 있던 Chrome.lnk파일을 복사해서 SJM폴더에 넣었음으로 해당 시간이 맞음 시간 기준은 UTC +00
Accessed한 시간 타겟이 생성된 시간 – Chrome.exe파일의 생성시간 타겟이 수정된 시간 – Chrome.exe 파일의 수정된 시간 타겟에 접근한 시간 – Chrome.exe 파일에 대한 접근 시간
RelativePath 대상 파일의 상대 경로로 Program Files의 Google Chrome Application 폴더 내에 존재하는 chrome.exe의 경로를 보여줌
WorkingDirectory  타겟의 작업 디렉터리를 보여줌
LocalPath Lnk파일의 타겟의 경로를 보여줌
Link파일을 분석해서 얻을 수 있는 정보
25

## Page 26

링크 파일 분석04
TargetIDAbsolutePath Chrome.exe의 절대 경로
머신ID와 MAC주소의 정보
트레커 생성 시간 또한 알려줘서 파일의 변경이 언제 이뤄졌는지도 알려줌
볼륨의 시리얼 정보
파일의 속성정보
내 PC의 머신ID를 확인한 모습 (일치함)
Link파일을 분석해서 얻을 수 있는 정보
26

## Page 27

링크 파일 분석의 한계05
RegistryExplorer.exe파일을
 일반 삭제한 경우
RegistryExplorer.exe파일을
완전 삭제할 경우
Link파일 삭제 실험
.lnk File
Target
바로가기 생성
타겟 일반 삭제
타겟 완전 삭제
결과비교
LNK 파일이 단순히 대상 파일에 대한 '링크'일 뿐, 실제 파일의 내용을 포함하고 있지 않다는 것
실험 목적
27
