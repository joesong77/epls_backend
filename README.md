# 環保小尖兵後端開發-Docker實作Container的作業

## 產生 Flask image 指令
```
docker image build -t dockerfile_test .   
```
## 透過 image 產生隔離的執行環境
```
docker run -d -p 3000:3000 --name docker0109 dockerfile_test
```
