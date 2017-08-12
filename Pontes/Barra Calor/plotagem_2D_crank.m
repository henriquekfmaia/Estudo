%plotagem
%plotagem perfil de temperatura inicial
subplot(2,2,1);
surf(T(:,:,1))
title('Temperatura no tempo inicial')
xlabel('X')
ylabel('Y')
zlabel('Temperatura')

%plotagem perfil de temperatura final
subplot(2,2,2);
surf(T(:,:,Tempo))
title('Temperatura no tempo final')
xlabel('X')
ylabel('Y')
zlabel('Temperatura')

%plotagem fonte de calor na placa
subplot(2,2,3);
surf(Q)
title('Fonte de calor na barra')
xlabel('X')
ylabel('Y')
zlabel('Temperatura')

%plotagem parametro L1 (velocidade de iteracao)
subplot(2,2,4);
semilogy((10:10:Tempo),L1)
title('L1 (velocidade de iteração)')
xlabel('Tempo')
ylabel('L1 [num de iteracoes/unidade de tempo]')

