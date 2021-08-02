while getopts n:u: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
	u) username=${OPTARG};;
    esac
done

echo "Config: $name";
echo "Superuser name: $username"


echo $name > /etc/hostname

adduser $username
usermod -aG sudo $username



shutdown -r now
