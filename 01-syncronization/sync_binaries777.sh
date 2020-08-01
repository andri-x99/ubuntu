
# AMBIL VIRUS
rsync -avz -e "ssh -i /root/.ssh/id_rsa"  pi@10.33.109.242:/opt/dionaea/var/lib/dionaea/binaries777/ /home/ubuntu/binaries777_from_dionaea

# LOG
echo "Success Get Virus!" $(date +%d-%m-%Y)
