fwd_anchor='';
rev_anchor='';
target_seq='ATGATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCTTTTGATAAAGAAACCTTTAAATCTATTACAAGTAAAGGTAAGATTCCACATATTATTCTTCATTCTCCTTCTCCA';
counts=zeros(32, numel(target_seq)/3);
cod=['GAA';'GAT';'AAA';'CGT';'CAT';'CCA';'CAA';'AAT';'ACT';'TCT';'GCA';'GGT';'ATG';'TGT';'GTT';'ATT';'CTG';'TAT';'TTT';'TGG';'TAG']; fclose all;
fid=fopen('C:\Users\sidni\Documents\Pool1Twist.sh','w');
for i=1:3:numel(target_seq)
    tmp=target_seq;
    for j=1:21
        tmp(i:i+2)=cod(j,:);
        fprintf(fid,'%s\n',['grep -c ' ([fwd_anchor tmp]) ' P1inp.fastq >> Pool1inptwist.txt']);
    end
    disp(num2str(i));
end
fclose(fid);
