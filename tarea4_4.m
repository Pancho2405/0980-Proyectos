n=-3:7;
x=0.55.^(n+3);
h=[1 1 1 1 1 1 1 1 1 1 1];
y=conv(x,h);
subplot(311)
stem(x)
title ('señal original')
subplot(312)
stem(h)
title ('Respuesta al impulso/ segunda señal')
subplot(313)
stem(y)
title ('Convolucion resultante')

