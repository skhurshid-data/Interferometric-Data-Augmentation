clear
close all
clc
Array=csvread('E:\codes\DATA04.CSV');
col2 = Array(:, 2);
%col2 = Array(1:250000,2);
%col2 = Array(250000:500000,2);
%col2 = Array(500000:750000,2);
% col2 = Array(750000:1000000,2);

% start = [0.1,0.7,1.3,1.9,2.5,3.1,3.7,4.3,4.9,5.5,6.1,6.7,7.3,7.9,8.5,9.1,9.4];
% End   = [0.7,1.3,1.9,2.5,3.1,3.7,4.3,4.9,5.5,6.1,6.7,7.3,7.9,8.5,9.1,9.7,10.0];
start = [0.1:0.10:9.9];
End = [0.20:0.10:10];

for i=1:length(start)
ymaxlim = max(col2(start(i)*10^5 : End(i)*10^5));
yminlim = min(col2(start(i)*10^5 : End(i)*10^5));
ymaxlim = ymaxlim + 40 * (ymaxlim/100);
yminlim = yminlim + 40 * (yminlim/100);
figure
z = plot(col2, 'Linewidth',0.6);
f = gca;
xlabel('Time (s)');
ylabel('Amp. (au)');
f.FontWeight = 'bold';
f.FontSize = 20;
f.LineWidth = 4;
%%axis([-1 -0.98 -0.02 0.02])
        xlim([start(i)*10^5 End(i)*10^5]);
        ylim([yminlim ymaxlim]);
        %ylim([-13*10^-3 13*10^-3])
        name_experimental = ['Exp_signal_data04_ ',num2str(i+j-1),'.png'];
        exportgraphics(gcf,name_experimental, 'Resolution',600)
end
