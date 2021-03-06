1. RNN

   **순환 인공 신경망** (**RNN**)은 [인공 신경망](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5%EC%8B%A0%EA%B2%BD%EB%A7%9D)의 한 종류로, 유닛간의 연결이 [순환](https://ko.wikipedia.org/wiki/%EC%88%9C%ED%99%98_(%EA%B7%B8%EB%9E%98%ED%94%84_%EC%9D%B4%EB%A1%A0))적 구조를 갖는 특징을 갖고 있다. 이러한 구조는 시변적 동적 특징을 모델링 할 수 있도록 신경망 내부에 상태를 저장할 수 있게 해준다. [전방 전달 신경망](https://ko.wikipedia.org/w/index.php?title=%EC%A0%84%EB%B0%A9_%EC%A0%84%EB%8B%AC_%EC%8B%A0%EA%B2%BD%EB%A7%9D&action=edit&redlink=1)과 달리, 순환 인공 신경망은 내부의 [메모리](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EB%A6%AC)를 이용해[시퀀스](https://ko.wikipedia.org/wiki/%EC%8B%9C%ED%80%80%EC%8A%A4) 형태의 입력을 처리할 수 있다. 따라서 순환 인공 신경망은 필기체 인식이나 [음성 인식](https://ko.wikipedia.org/wiki/%EC%9D%8C%EC%84%B1_%EC%9D%B8%EC%8B%9D)과 같이 시변적 특징을 가지는 데이터를 처리할 수 있다.

2. **GRU(Gated Recurrent Unit)**가 궁금하신 분...
   일단 안 중요해 보여서 스킵.

3. RNN(기본구조에서) 으로 할 수 있는 것들

   - 사진 하나를 네트워크에 넣어서 키워드 여러개 뽑아내기
     - 풍경화 -> 나무, 따스함, 저녁 

   - 단어 여러개를 넣어서 감성 점수 뽑아내기

     - 씨발, 병신, 개같은 -> 화남

   - 단어 여러개로 단어 여러개 뽑아내기(번역)

     - I, am, student -> 나, 는, 학생

     **왜** 랑 **어떻게**는 아직 모르겠음, RNN은 기본적으로 순차적으로 등장하는 데이터 처리에 적합한 모델이다. 이는 앞에 있는 데이터들 간의 연관성을 잘 추론해낸다는 뜻으로 봐도 무방할 듯? 또 1:1, 1:N, N:1 처럼 인풋 아웃풋의 사이즈가 자유로워서 구조를 유연하게 짤 수 있다는 것도 RNN의 장점

4. RNN은 히든 노드가 방향을 가진 엣지로 연결돼 순환구조를 이루는(directed cycle) 인공신경망의 한 종류입니다

   방향을 가진 엣지로 연결되었기 때문에 순전파가 가능하고 이 과정에서 RNN 기본 구조가 스스로를 재사용하도록 생겨먹음에 따라 순환구조를 이루게 된다. 

   엣지가 뭐지? 뉴럴네트워크 노드같은 느낌이네. 일단 스킵

5. RNN의 기본 구조.

   [![source: imgur.com](http://i.imgur.com/s8nYcww.png)](http://imgur.com/s8nYcww)

   녹색 박스는 히든 state를 의미. 빨간 박스는 인풋, 파란 박스는 아웃풋. 왜 가설함수(활성함수)가 저렇게 생겨먹었는지는 아직 모르겠음. tanh함수는 찾아보니 시그모이드랑 비슷하게 생겨먹음(나중에 찾아보니 시그모이드랑 하이퍼볼릭이랑 같이 가장 많이 쓰이는 2대장이었음, 그 밖에 렐루..), 어쨋든 알아 둬야 할 건 이전 h에 영향 받아 현재 h가 갱신된다는 점.

6. 활성함수로 비선형함수를 쓰는 이유? 
   활성함수는 말 그대로 의미를 이해하면 편하다. 인풋으로 들어온 값이 아웃풋을 도출해 내는 데 있어 의미가 있냐 없냐를 따지기 위한 함수다. 이를테면 씨발, 병신, 개같은 -> "화남"을 뽑아내는 메커니즘이 있다고 할 때, "너 때문에" 같은 단어는 "화남"을 뽑아내기에는 영향력이 그리 크지 않은 단어다. 시스템적으로 활성함수는 입력신호의 총합을 출력신호로 변환하는 함수인데, 초창기 모델인 퍼셉트론에서는 이런 게 없었고, 뉴럴 네트워크에 들어와서야 등장한다.
   본론으로 돌아와서, 활성함수로 비선형 함수를 쓰는 이유는 레이어가 의미를 갖게 하기 위해서다. 선형함수는 y = ax + b같은 애들인데, 예네들로 구성된 층을 여러개 해봤자 f(f(f(x))) = a(a(ax + b) + b) + b 이므로 x의 승수는 어쨌거나 1이 된다. 이는 곧 레이어가 100만개든 한 개든 웨이트를 잘 조절하면 가설함수를 만들수 있다는 뜻, 다시 말해 레이어를 쌓아봤자 의미가 없다라는 것이다. 하지만 레이어를 왜 쌓아야 하는가는 잘 모르겠음.

7. character-level-model

   다음 글자를 예측하기 위한 모델.

8. RNN과 파라미터

   RNN도 정답을 필요로 한다. 네트워크에 정답을 알려주어야 파라미터를 조절해서 학습되지 않은 데이터가 들어왔을 때도 잘 동작하게 된다. 파라미터를 업데이트하기 위해서는 역전파라는 걸 수행한다.

   RNN이 학습하는 파라미터는 인풋을 히든레이어로 보내는 wx, 이전 히든 레이어에서 다음 히든 레이어로 보내는 wh, 히든 레이어레서 아웃풋으로 보내는 wy 이다. 그리고 모든 시점의 state에서 이 parameter는 동일하게 적용된다.

9. 역전파
  계산그래프와 chain rule

  1. chain rule은 편미분 공식을 말하는 거다. dL/dx = dy/dx * dL/dy

  **계산그래프(computational graph)**는 계산과정을 그래프로 나타낸 것. 

  **노드(node, 꼭지점**는 함수(연산),

  **엣지(edge, 간선)**는 값. 

  아래는 y=f(x)를 나타내는 계산그래프.

   [![source: imgur.com](http://i.imgur.com/o8Q7slz.png)](http://imgur.com/o8Q7slz)

    뉴럴네트워크는 위와 같은 녀석들이 졸라 많이 모여있는 집합이다. 위와 같은 녀석들을 모두 통과하고 나면 네트워크에서는 결과를 던져주는데, 우리는 우리가 기대한 값과 이 결과값의 차이가 클 수록 많이 실망할 것이다. 이 경우 우리는 네트워크가 더 나은 방향으로 학습할 수 있도록 차이값인 Loss를 구해 네트워크에 다시 피드백을 해주어야 하는데, 위 그림에서는 Loss가 L로 나타내어졌다. 

  여기서 왜 편미분한 값을 뒤로 전달할까? 그 답은 그레디언트 디센트에 있다. GD는 이제 더 좋은 게 뭐 워낙 많이 나와서 요새 잘 쓰이지도 않는 것 같지만, 어쨌든 세타(웨이트)를 업데이트 하는 와중에 학습률에 편미분값을 곱해서 빼기 때문에 위에서도 편미분한 값을 뒤로 전달해 웨이트를 업데이트 시키는 것이다. 다른 ADAM이나 그런 것들은 어떻게 하는 지 현재는 잘 모르겠다. 같은 맥락이라면 그런 것들도 편미분 값을 전달하지 않을까?

10. RNN의 활성함수는 왜 저따위로 생겼나

  RNN은 기본적으로 시퀀스적인 데이터를 받아들려 학습하기 위해 만들어졌다. 시퀀스라는 것 순차적인 데이터를 뜻한다. 만약 t 시간일때 받아들인 데이터를 독립적으로 처리한다면 순차적인 데이터를 커버할 순 없을테니, RNN은 t-1시간일때의 정보도 받아들이는 쪽을 택했다. 하지만 이 t-1일때의 정보 역시 t-2일 때의 정보까지 담고 있을테니, 결국 t 시간일 때의 데이터 처리는 이전까지의 데이터를 모두 들여다 보고 학습하는 게 된다(하지만 편미분 하면서 오래된 데이터일 수록 그 영향은 점점 미비해진다. 그래서 LSTM이 나온거). 어쨌든 이를 바탕으로 생각해보면, x -> y 만을 처리하는 기본 노드에서는 이전 데이터를 받아들이는 간선이 없으므로, x -> h -> y 구조를 만들었다. h로 이전 단계에 학습했던 데이터를 처리하기 위해서다. 결국 h가 recurrent하게 이 전 단계의 정보를 받아들이게 된다. 
  x, h, y에서 우리는 x는 이미 알고 있으므로 h, y만 알면 된다. x -> h일 때 전달되는 게 U, (이전)h -> h 에 전달되는 게 W, h ->y 로 전달되는 게 V라고 하면, y = (Vh + bias) 가 되고 , h = f(Ux + W(이전)h + bias) 가 된다.

11. RNN의 역전파

[![source: imgur.com](http://i.imgur.com/XYDxsNs.png)](http://imgur.com/XYDxsNs)

12. LSTM의 기본 구조

[![source: imgur.com](http://i.imgur.com/H9UoXdC.png)](http://imgur.com/H9UoXdC)

13. RNN과 LSTM 차이
   ![source: imgur.com](http://i.imgur.com/jKodJ1u.png)
   별 반 차이 없다. 히든 스테이트를 업데이트 하는 로직만 바뀌었을 뿐이다. 그 외엔 다른 곳을 건드릴 필요도 없는 게, 이전 데이터를 기억하는 놈은 히든 스테이트 하나 뿐이기 때문이다.

   주목할 만한 점은 다음 h 로 들어가는 값이 RNN에서는 1개이지만 LSTM에서는 2개 라는 것이다. 위에 들어가는 값은 Cell state라고 부르는데, 하는 역할은 딱 컨베이어 벨트다. LSTM을 쭉 펼쳐놓고 보면 처음 부터 끝까지 컨베이어 벨트처럼 관통한다. 

   박스 안을 유심히 살펴보면 h가 시그모이드(노란색 델타)를 거친다음 들어오는 값에 곱하기 노드를 붙여놨는데, 이 값이 0이면 전달이 안되고 1이면 전달이 된다. 절반이면 반쯤 중요하단 뜻이겠지.
