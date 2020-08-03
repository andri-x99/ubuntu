
# AMBIL VIRUS
rsync -avz -e "ssh -i /root/.ssh/id_rsa"  pi@10.33.109.242:/opt/dionaea/var/lib/dionaea/binaries/ /home/ubuntu/binaries_from_dionaea

# LOG
echo "Success Get Virus!" $(date +%d-%m-%Y)
