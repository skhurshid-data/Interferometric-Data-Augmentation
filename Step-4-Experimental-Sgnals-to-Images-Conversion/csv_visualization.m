% clear
% close all
% clc
Array=csvread('E:\Thesis data\fringe detection\DATA04\DATA04.CSV');
%col1 = Array(:, 1);
%col2 = Array(:, 2);
col2 = Array(:, 2);
%z= plot(col1, col2)
figure
z = plot(col2, 'Linewidth',0.6);
%axis([-1 -0.98 -0.02 0.02])

        xlim([0.8*10^4 2.2*10^4])
        ylim([-0.01 0.01])
        %ylim([-13*10^-3 13*10^-3])
        name_experimental = ['Exp_signal ',num2str(i+j-1),'.png'];
        saveas(gcf,name_experimental)
        
%for i (0:1000)
%     m = max col2[1:1000]