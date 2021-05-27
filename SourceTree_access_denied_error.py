# 사용자 계정 오류 : "remote http basic access denied sourcetree"

# git 자체의 오류의 경우, cmd 창에서 control /name Microsoft.CredentialManager 를 통해 
# credential manager를 실행시켜 계정정보를 삭제 후 재등록하면 된다.
# 혹은 관리자 권한으로 실행한 cmd 등에서 'git config --system --unset credential.helper'를 통해 업로드

# 단, SourceTree의 경우 이렇게 해도 삭제되지 않으며 추가적이 작업이 필요하다.
# Window의 경우, C: 아래 User(상용자) 아래 실제 사용자 폴더에서 보기 옵션을 숨긴 파일 표시로 설정해야 appdata 폴더가 보이고
# Appdata 폴더 아래 Local > Atlassian > SouceTree 폴더에서 userhosts 파일과 passwd 파일을 제거하면 sourcetree에 저장된 모든 계정 정보가 제거되어 새로 등록할 수 있다.
