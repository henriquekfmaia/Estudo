%Equacao Temperatura - Cranck Nicholson
d = 1; %deltat
alpha = 10^-4; %difusividade termica (Cobre)
N = 40; %(numero de pontos na coordenada x)
M = 40; %(numero de pontos na coordenada y)
L = 1; %comprimento da placa (m) - valor maximo em x
W = 1; %largura da placa (m) - valor maximo em y
dx = L/(N-2); %deltax em funcao do numero de pontos da malha e do comprimento, L, da placa
dy = W/(M-2); %deltay em funcao do numero de pontos da malha em y e da largura, W, da placa
Kx= (alpha*d)/(dx^2);%constante da derivada parcial em x
Ky= (alpha*d)/(dy^2);%constante da derivada parcial em y

T1 = 10; %temperatura na extremidade x=0 da placa
T2 = 10; %temperatura na extremidade y=0 da placa
T3 = 10; %temperatura na extremidade x=L da placa
T4 = 10; %temperatura na extremidade y=W da placa

%i -> linhas da matriz (variar i corresponde a andar na direção y)
%j -> colunas da matriz (variar j corresponde a andar na direção x)
%contador em tempo: n

tempo = 10000; %numero de iteracoes de tempo
densidade = 8.92; %densidade do material da placa(cobre) [g/cm³]
Cv = 0.09; %calor especifico do material da placa(cobre) [cal g^-1 C^-1]
Qponto = [];

%criacao do vetor 'x' cartesiano -> com mesmo numero de pontos da malha em
%x (com menor valor = -N/2)
x=[-N/2]; 
for j=1:N
    if j ~=1
        x(j)= x(j-1)+1;
    end
end

%criacao do vetor 'y' cartesiano -> com mesmo numero de pontos da malha em
%y (com menor valor = -N/2)
y=[-M/2];

for i=1:M
    if i ~=1
        y(i)= y(i-1)+1;
    end
end


%criacao da malha de pontos do plano cartesiano
[X,Y]=meshgrid(x,y);

%criacao de funcao Z(X,Y) continua no plano cartesiano -> ver alguns casos abaixo:

Z1 = -25+30*((X.^2)-(Y.^2)); %paraboloide hiperbolico

Z2 = 10+200*(Y); %fonte de calor linear

Z3 = -30*((X.^2)+(Y.^2)); %paraboloide eliptico

Z4 = 100*ones(N,M); %temperatura constante

Z5 = sqrt((X.^2)+(Y.^2)-(0.125*(M+N))^2); %hiperboloide de uma folha - lado positivo




%perfil de temperaturas (faz-se necessario para caso queiramos fazer
%distribuiçao descontínua de temperaturas)

%perfil de temperaturas (faz-se necessario para caso queiramos fazer
%distribuiçao descontínua de temperaturas)
for i = 1:M
    for j = 1:N
         %fonte de calor como funcao da posicao
        if imag(Z4(i,j))==0 %considerar apenas resultados reais da funcao Z
            Qponto(i,j) = Z4(i,j);
        else %caso z assuma valores complexos estes serao armazenados como especificado abaixo
            Qponto(i,j) = 0;
        end
    end
end



Q = (1/densidade*Cv)*Qponto; %fonte de calor Q nos pontos da malha


L1 = [];
L1(1) = 1;
Tempo = 1; %Tempo maximo de iteracoes
T = ones(L,W,tempo);

            
            %criacao do caso inicial  geracao de aleatorio no inicio,
            %observando as condições de contorno do sistema:
for i=2:M-1
    for j=2:N-1
        T(i,j,1) = 25 +10*randn(1,1);
    end
end

for i=2:M-1
        T(i,1,1) = 2*T1 - T(i,2,1);
        T(i,N,1) = 2*T3 - T(i,N-1,1);
end
for j=2:N-1
    T(1,j,1) = 2*T2 - T(2,j,1);
    T(M,j,1) = 2*T4 - T(M-1,j,1);
end

    T(1,1,1) = 0;
    T(N,1,1) = 0;
    T(N,M,1) = 0;
    T(1,M,1) = 0;

    
%criação das matrizes NxN e MxM usadas na equacao matricial de cada iteração de linha e/ou coluna [N1 e N2 -> NxN; M1 e M2 -> MxM; M1b -> inv(M1); N1b = inv(N1)]    
N1 = zeros(N,N); N2 = zeros(N,N);
M1 = zeros(M,M); M2 = zeros(M,M);

%montagem das matrizes N1 e N2 dos coeficientes da equacao N1*T(n+1/2) = N2*T(n) 
for p=1:N
    if p == 1
        N1(p,p) = 1; 
        N1(p,p+1) = 1; 
        N2(p,p) = 1;
        N2(p,p+1) = 1;
    elseif p == N
        N1(p,p)=1; 
        N1(p,p-1)=1; 
        N2(p,p) = 1;
        N2(p,p-1)=1;
    else
        N1(p,p-1) = -0.25*Kx; N1(p,p+1) = -0.25*Kx;
        N1(p,p) = (1+0.5*Kx);
        N2(p,p-1) = 0.25*Kx; N2(p,p+1) = 0.25*Kx;
        N2(p,p) = -0.5*Kx;
    end
end

for p=1:M
    if p == 1
        M1(p,p) = 1; M1(p,p+1) = 1; M2(p,p) = 1; M2(p,p+1) = 1;
    elseif p == M
        M1(p,p)=1; M1(p,p-1)=1; M2(p,p) = 1; M2(p,p-1) = 1;
    else
        M1(p,p-1) = -0.25*Ky; M1(p,p+1) = -0.25*Ky;
        M1(p,p) = (1+0.5*Ky);
        M2(p,p-1) = 0.25*Ky; M2(p,p+1) = 0.25*Ky;
        M2(p,p) = -0.5*Ky;
    end
end


TM = ones(N,M); %matriz correspondente a T no tempo (n + meio);
Tk = T(:,:,1); %matriz Tk corresponde ao valor antigo da Temperatura para as linhas ou colunas analisadas;
E1=zeros(1,N);
F1=zeros(1,M);
Tempo = 1;
s=1;%indices para o vetor L1
L1=[1];%vetor que armazena os termos de velocidade (variacao normalizada dos valores de temperatura por dt/2)
for n = 2:tempo-1
    for i = 2:M-1
        TM(i,:)=T(i,:,n-1); 
        Tk(i,:)=2*TM(i,:);
        
        while [(sum(abs(TM(i,:)-Tk(i,:))))/sum(abs(TM(i,:)))] > 0.005*d
            Tk(i,:)=TM(i,:);
            
            for b=2:N-1
                E1(b)= 0.25*Ky*[T(i-1,b,n-1)-2*T(i,b,n-1)+T(i+1,b,n-1)+Tk(i-1,b)-2*Tk(i,b)+Tk(i+1,b)]+T(i,b,n-1) + d*Q(i,b);
            end
            
            E = N2*(T(i,:,n-1))'+E1';
            TM(i,:) = (N1\E)';
            if i==2
                TM(1,:)=2*T2*ones(1,N)-TM(2,:);
            elseif i==M-1
                TM(M,:)=2*T4*ones(1,N)-TM(M-1,:);
            end
                
        
            
        
        end
        
        
    end
    
    for j=2:N-1
        T(:,j,n)=TM(:,j); Tk(:,j)=2*T(:,j,n);
        
        while [(sum(abs(T(:,j,n)-Tk(:,j))))/sum(abs(Tk(:,j)))] > 0.005*d
            Tk(:,j)=T(:,j,n);
            for b=2:M-1
                F1(b)= 0.25*Kx*[Tk(b,j-1)-2*Tk(b,j)+Tk(b,j+1)+TM(b,j-1)-2*TM(b,j)+TM(b,j+1)] + TM(b,j) +d*Q(b,j);
            end
            F = M2*TM(:,j)+ F1' ;
            T(:,j,n) = M1\F;
            if j == 2
                T(:,1,n) = 2*T1*ones(M,1)-T(:,2,n);
                
            elseif j == N-1 
                T(:,N,n)=2*T3*ones(M,1)-T(:,N-1,n);
                
            end
            T(1,:,n)=2*T2*ones(1,N)-T(2,:,n);
            T(M,:,n)=2*T4*ones(1,N)-T(M-1,:,n);
                
            
                
            
        end
    end
    
    Tempo = n; %maior tempo armazenado
    if n>1
        if rem(n-1,10)==0 %para o tempo inicial e a cada 10 interacoes, testar se o equilíbrio foi atingido antes de completar o numero de iteracoes estabelecido inicialmente(conferir se satisfaz a condição de parada);
            L1(s) = (2/d)*(sum(abs(T(:,:,n)-T(:,:,n-10))))/sum(abs(T(:,:,n))); %condicao para o caso anterior: caso a diferenca entre o ultimo vetor armazenado e o vetor armazenado a 10 passos de tempo antes tenha modulo proximo de zero, o programa sai do loop de tempo;
            if  L1(s) < 0.000001; 
                break
            end
            s = s+1;
        end
    end
    

    
    n = n+1;
end
T(1,1,Tempo)=10;
T(1,N,Tempo)=10;
T(M,1,Tempo)=10;
T(M,N,Tempo)=10;

