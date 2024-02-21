# 12장. 암호화

# 1. 암호화 살펴보기

## 1. 가장 약한 연결고리의 중요성 이해하기

- 개별 요소의 보안에 집중한 나머지 체계의 전체 보안을 소홀히 하는 경향
- 시스템이 가진 허점과 취약점 일부를 해커들이 악용하여 민감한 정보 탈취 가능성 존재

## 2. 기본 용어

- 암호(Cipher) : 일련의 정보를 암호화하거나 해독하는 알고리즘
- 원문서(Plain Text) : 텍스트 파일, 동영상, 비트맵 또는 디지털화된 음성
- 암호문(Cipher Text) : 원문서를 암호화한 결과
- 암호화 스위트(Cipher Suite) : 암호화 소프트웨어 묶음
- 암호화(Encryption) : 원문서를 암호문으로 변환하는 과정
- 해독(Decryption) : 암호문을 원문서로 되돌리는 과정
- 암호 분석(Cryptanalysis) : 암호에 대한 정보 없이 암호문을 원문서로 되돌리는 시도를 통해 암호 함수의 성능 분석
- 개인 식별 정보(Personally Identifiable Information, PII) : 독자적으로 또는 다른 정보 와의 결합을 통해 개인을 식별할 수 있는 정보

## 3. 보안 요구사항 이해하기

### 1. 요소 이해하기

- 어떤 애플리케이션을 보호해야 하는가
- 누구로부터 애플리케이션을 보호해야 하는가
- 애플리케이션을 보호해야 하는 환경은 어떤 것인가
- 왜 애플리케이션을 보호해야 하는가

### 2. 보안 목표 설정하기

- 인증(Authentication) : 사용자가 스스로 주장하는 신원이 맞는지 확인
- 기밀성(Confidentiality) : 인증된 사용자에게만 민감한 데이터에 접근할 수 있게 하는 개념
- 무결성(Integrity) : 데이터를 전송하거나 저장하는 동안 데이터가 어떤 식으로든 변형되지 않았다는 것을 확인하는 절차
- 부인방지(Non-Repudiaion) : 발신자는 정보가 제대로 수신됐음을 확인하고 수신자는 발신자의 신원을 확인받는 개념

### 3. 데이터 민감성 이해하기

- 공개 데이터 : 모두가 사용할 수 있도록 공개된 데이터
- 내부 데이터 : 대중에 공개하지 않았으나 공개한다고 해서 해로운 결과를 초래하지는 않는 것
- 민감한 데이터 : 대중적으로 공개하지 말아야 하거나 공개한다면 개인 또는 집단에 피해를 끼칠 수 있는 데이터
- 매우 민감한 데이터 : 특급 기밀 데이터(Top-Secret Data), 데이터가 누출되면 해당 조직에 매우 큰 타격을 입힐 수 있는 것

## 4. 기본적인 암호 설계 이해하기

- 악의적인 프로그램이나 권한이 없는 사용자로부터 민감한 정보를 보호하기 위해서 데이터 변환하는 것

### 1. 대치 암호(Substitution Cipher)

- 미리 정해둔 방법으로 원문서의 글자를 다른 글자로 바꾸는 간단한 방식
- 각 글자에 대응되는 글자 설정
- 설정한 방식을 통해 원문서의 글자를 다른 글자로 변환
- 암호를 해독하기 위해 대응 관계를 반대로 적용해 원문서 복원
- 시저 암호(Caesar Cipher) : 각 글자를 오른쪽으로 세 번째에 있는 글자로 대체

    ```python
    import string
    
    rotation = 3
    P = 'CALM'
    C = ''
    for letter in P:
        C = C + (chr(ord(letter) + rotation))
    
    print(C)
    ```

- 로테이션 13(ROT13) : 각 글자를 오른쪽으로 13번째에 위치한 글자로 바꿈

    ```python
    import codecs
    
    P = 'CALM'
    C = ''
    C = codecs.encode(P, 'rot_13')
    
    print(C)
    ```

- 대치 암호의 암호 분석 : 글자 이동 간격을 테스트하여 암호 해독 가능

### 2. 전치 암호(Transposition Cipher)

- 사용할 행렬의 크기 결정
- 원문서에 있는 글자를 행렬에 가로 방향으로 채워 넣음
- 행렬에 채워진 글자들을 세로 방향으로 읽음

# 2. 암호화 기법의 종류 이해하기

## 1. 암호화 해시 함수 사용하기

- 메시지 고유의 지문을 생성하는 수학적 함수
- 원문서로부터 해시라 칭하는 고정된 크기의 출력 생성
- 결정론적, 동일한 원문서는 동일한 해시 생성
- 고유한 입력 문자열은 고유한 출력 해시값을 생성
- 입력 메시지의 길이에 관계없이 해시의 길이는 고정
- 원문서가 조금이라도 변형되면 해시값이 달라짐
- 해시 함수는 단방향 함수 → 암호문을 이용해 원문서 생성 불가

### 1. 암호화 해시 함수 구현하기

- MD5 : 128비트 해시 생성, 비교적 단순한 알고리즘

    ```python
    myHash = md5_crypt.hash('myPassword', salt='xE2')
    md5_crypt.verify('myPassword', myHash)
    md5_crypt.verify('myPassword2', myHash)
    ```

- SHA(Secure Hash Algorithm) : 안전한 해시 알고리즘

    ```python
    from passlib.hash import sha512_crypt
    
    sha512_crypt.using(salt='qIo0foX5', rounds=5000).hash('myPassword')
    
    myHash = sha512_crypt.using(salt='qIo0foX5', rounds=5000).hash('myPassword')
    ```


### 2. 암호화 해시 함수의 활용 사례

- 파일을 복제했을 때 원본과 동일한지 확인하는 데 사용

## 2. 대칭 암호화

- 암호화와 해독 과정에서 동일한 키를 사용

### 1. 대칭 암호화 코딩하기

```python
import cryptography as crypt
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('mykey.key', 'wb')
file.write(key)
file.close()

file = open('mykey.key', 'rb')
key = file.read()
file.close()

from cryptography.fernet import Fernet

message = 'Ottawa is really cold'.encode()
f = Fernet(key)
encrypted = f.encrypt(message)

decrypted = f.decrypted(encrypted)

print(decrypted)
```

### 2. 대칭 암호화의 장점

- 대체로 비대칭 암호화에 비해 훨씬 빠름

### 3. 대칭 암호화의 문제점

- 두 사용자 또는 두 프로그램이 대칭 암호화를 이용해 통신하려면 보안 채널로 키를 주고받아야 함
- 키 보안 : 대칭 암호화 키를 어떻게 보호한 것인가
- 기 분배 : 대칭 암호화 키를 다른 위치로 어떻게 전송할 것인가

## 3. 비대칭 암호화(Asymmetric)

- 보기에는 서로 완전히 다르지만 알고리즘적으로 연결된 두 키를 생성
  - 프라이빗 키 : 해당 정보의 주인만 접근 가능
  - 퍼블릭 키 : 누구든 열람해도 상관없음
- 두 키 중 하나로 정보를 암호화 → 이를 해독할 수 있는 유일한 방법은 나머지 키 사용

### 1. SSL(Secure Sockets Layer)/TLS(Transport Layer Security) 핸드셰이크 알고리즘

- SSL : 본래 HTTP에 보안을 추가하기 위해 개발
- TLS : HTTP가 안전한 통신 세션을 만드는 방식의 근간
  - 클라이언트가 서버에 메시지를 보냄
    - 사용하는 TLS 버전
    - 클라이언트가 지원하는 암호 스위트 목록
    - 압축 알고리즘
    - byte_client로 식별할 수 있는 무작위 바이트 문자열
  - 서버는 클라이언트에 답장을 보냄
    - 클라이언트가 제공한 목록 중 서버가 선택한 암호 스위트
    - 세션 ID
    - byte_client로 식별할 수 있는 무작위 바이트 문자열
    - 서버의 퍼블릭 키를 포함하고 있는 cert_server로 식별할 수 있는 서버 디지털 인증서
    - 허용하는 클라이언트 인증의 식별 가능한 이름
    - 지원하는 인증서 유형
  - 클라이언트가 cert_server 검증
  - 클라이언트가 byte_client2로 식별되는 무작위 바이트 문자열 생성, 서버로부터 cert_server를 통해 받은 퍼블릭 키로 암호화
  - 클라이언트가 무작위 바이트 문자열을 만들고 이를 자신의 프라이빗 키를 이용해 암호화
  - 서버가 클라이언트 인증서 검증
  - 클라이언트가 프라이빗 키로 암호화한 메시지 서버에 전송
  - 서버에서 확인 → 서버는 프라이빗 키로 암호화된 메시지를 클라이언트에 전송

### 2. 퍼블릭 키 인트라

- 암호화 키를 관리할 때 가장 널리 사용되는 안정적인 방법
- 개인과 조직에 따라 다른 기준을 적용하여 신원 확인