t=-0.04:0.001:0.04;
x=20*exp(j*(80*pi*t-0.4*pi));
%plot3 (t,real(x),imag(x)); grid
%title('20*e^{j*(80\pit-0.4\pi)}')
%xlabel ('tiempo, s'); ylabel('real'); zlabel('imag')
plot (t, real(x), 'b'); hold on
plot (t, imag(x), 'r'); grid
title('rojo-componente imaginario, Azul-Componente real de la exponencial')
xlabel('Tiempo'); ylabel('Amplitud')
