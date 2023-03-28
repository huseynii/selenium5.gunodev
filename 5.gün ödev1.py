
Pytest, bir Python test çerçevesidir ve test fonksiyonlarının yanı sıra özellikle pytest modülünde tanımlanmış bir dizi decorator (süsleyici) sağlar. Bu decorator'lar testlerin davranışını değiştirir, test sonuçlarını filtreler ve hatta test sonuçlarının raporlanmasını özelleştirmenize yardımcı olur.

@pytest.fixture Bir test işlevi, fikstür adından bir giriş parametresi olarak bahsederek bir fikstür kullanabilir. Testlere girdi sağlayan fikstür fonksiyonu oluşturulur.Fikstür işlevine erişmek için testlerin, fikstür adını giriş parametresi olarak belirtmesi gerekir.

@pytest.mark.skipif() Koşullu olarak testleri atlamak için kullanılır

@pytest.mark.skip kullanılarak testler atlatılıyor

@pytest.mark.parametrize kullanarak testleri parametreleştirebiliriz

@pytest.mark.xfail testin başarısız olmasını beklediğimiz durumlarda kullanılır

@pytest.mark.timeout() Testin zaman aşımı yönetimi için kullanılır