clear
close all
clc
load('exp_C_var_exemplar.mat'); %first data
%load('exp_C_var.mat'); %second data
%load('pillar_vibration_tek2_8_12_8.mat');
col2 = P;

%start = [0.01:0.005:9.995]; %for first data
%End = [0.015:0.005:10];  %for first data

 start = [0.1:0.10:9.1]; %for second data
 End = [0.11:0.10:10];  %for second data

for i=1:length(start)
ymaxlim = max(col2(start(i)*10^5 : End(i)*10^5));
yminlim = min(col2(start(i)*10^5 : End(i)*10^5));
ymaxlim = ymaxlim + 90 * (ymaxlim/100);
yminlim = yminlim + 90 * (yminlim/100);
figure
z = plot(col2, 'Linewidth',1.7);
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
        name_experimental = ['Exp_signal_c_var_ ',num2str(i+j-1),'.png'];
        exportgraphics(gcf,name_experimental, 'Resolution',600)
end

