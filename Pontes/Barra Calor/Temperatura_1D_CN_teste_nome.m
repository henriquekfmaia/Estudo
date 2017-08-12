%Barra delgada -- equacao de calor -- Cranck Nicholson
d = 1; % Delta t
a = 3*10^(-5); %Difusividade termica
X = 20; %Numero de pontos em X
L = 1; %Comprimento da barra
dx = L/(X-2); %dx em funcao do comprimento da barra L e do numero de pontos


T1 = 0; %Temperatura inicial em x=0
T2 = 0; %Temperatura inicial em x=L

tmax = 100000; %Limite de tempo
%Distribuicao de temperatura da fonte de calor
Q1 = zeros(X,1);
Q2 = 100*ones(X,1);

Q = Q1;
%Matriz Temperatura no ponto X x tempo (barra inicialmente uniforme)
T = 20*ones(X,tmax);

T(1,1) = T1; %Temperatura inicial em x=0
T(X,1) = T2; %Temperatura inicial em x=L

X1 = zeros(X,X);  %Matrizes M
X2 = zeros(X,X);

%montagem das matrizes X1 e X2 dos coeficientes da equacao X1*T(n+1/2) = X2*T(n) 
for p=1:X
    if p == 1
        X1(p,p) = 1; 
        X1(p,p+1) = 1; 
        X2(p,p) = 1;
        X2(p,p+1) = 1;
    elseif p == X
        X1(p,p)=1; 
        X1(p,p-1)=1; 
        X2(p,p) = 1;
        X2(p,p-1)=1;
    else
        X1(p,p-1) = -0.25*0.00972; X1(p,p+1) = -0.25*0.00972;
        X1(p,p) = (1+0.5*0.00972);
        X2(p,p-1) = 0.25*0.00972; X2(p,p+1) = 0.25*0.00972;
        X2(p,p) = -0.5*0.00972;
    end
end

T_ant = ones(X,1); %T anterior
T_calc = 2*ones(X,1); %T calculado (proximo, atual)

E1=zeros(1,X); %Matriz 'b'

for n=2:tmax
    for i=2:(X-1)
	    T(i,1,n) = T(i,1,n-1);    %Iguala o proximo ponto ao ponto anterior
	    T_ant(i,1) = 2*T(i,1,n);  %Iguala T_ant a 2*proximo ponto
		
		while ((abs(T(i,1,n)-T_ant(i,1)))/abs(T_ant(i,1))) > 0.005 %Enquanto diferenca entre T e T_ant for maior que 0,5%, a iteracao continua rodando
		    T_ant(i,1) = T(i,1,n);
		
		    %Cranck Nicholson
		    E1(i) = 0.25*0.00972*[T(i-1,1,n-1)-2*T(i,1,n-1)+T(i+1,1,n-1)+T_ant(i-1,1)-2*T_ant(i,1)+T_ant(i+1,1)]+T(i,1,n-1) + Q(i,1);
		
		    E = X2*(T(i,1,n-1))'+E1';
		    T(i,1,n) = X1/E;
		
		    if i == 2                  %Nao entendi essa serie de if (linha 66 a linha 70)
		        T(1,1,n) = 2*T1*ones(X,1)-T(2,1,n);
		    elseif i == (X-1)
		        T(X,1,n) = 2*T2*ones(X,1)-T(X-1,1,n);
		    end
		end
	end
	
	if rem(n-1,10) == 0 %A operacao sera feita a cada 10 iteracoes
	    dif = sum(abs(T(:,1,n) - T(:,1,n-10)))/sum(abs(T(:,1,n))); %Verifica se o equilibrio foi alcancado
	    if dif < 0.000001
		    tmax = n; %Diz que tmax e o tempo atual
	        break     %E para as iteracoes
	    end
	end
end
T(1,1,tmax) = T1;
T(X,1,tmax) = T2;