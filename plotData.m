close all
clear all
[d1 d2]=xlsread('./data/oecd-countries.xls');
ColNames= d2(1,:);
Countries= d2(2:end,1);
for ConditionToPlot=1:4;
[SortedSkillValue SortedSkillPos]=sort(d1(:,ConditionToPlot));
figure, bar(SortedSkillValue)
set(gca,'XTick',1:size(SortedSkillValue,1),...
    'XTickLabel',Countries(SortedSkillPos),...
    'XTickLabelRotation',45,'FontSize',10)
ylabel(ColNames(ConditionToPlot))
end