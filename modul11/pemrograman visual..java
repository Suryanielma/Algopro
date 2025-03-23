// public class Mobil {
//     String merek;
//     int tahunProduksi;

//     // Konstruktor Default
//     public Mobil() {
//         merek = "Toyota";
//         tahunProduksi = 2021;
//     }

//     // Konstruktor Parameter
//     public Mobil(String merek, int tahunProduksi) {
//         this.merek = merek;
//         this.tahunProduksi = tahunProduksi;
//     }

//     // Konstruktor Copy
//     public Mobil(Mobil mobil) {
//         this.merek = mobil.merek;
//         this.tahunProduksi = mobil.tahunProduksi;
//     }
// }





class Laptop{
    Laptop(){
        system.out.println("Satu object laptop sudah di buat")
    }
};

class BelajarJava{
    public static void main(string args[]){
        Laptop laptopAnto = new Laptop();
        Laptop laptopLisa = new Laptop();
        Laptop laptopRudi = new Laptop();
    }
}