print("🎭 Maligayang pagdating sa Bugtong-Bugtong! Subukan mong sagutin ang mga palaisipan!")

while True:
    start = input("\nGusto mo bang maglaro? (oo/hindi): ").lower()

    if start == "oo":
        while True:  
            print("\n📜 Unang Bugtong: Hindi pari, hindi hari, nagsusuot ng sari-sari. Ano ito?")
            ans1 = input("Sagot mo: ").lower()

            if ans1 == "sampayan":
                print("🎉 Tama! Sunod na bugtong!\n")
                print("📜 Puno ay buo, dahon ay dalawa. Ano ito?")
                ans2 = input("Sagot mo: ").lower()

                if ans2 == "tainga":
                    print("🎉 Galing! Susunod na bugtong!\n")
                    print("📜 Baboy ko sa pulo, balahibo'y pako. Ano ito?")
                    ans3 = input("Sagot mo: ").lower()

                    if ans3 == "lansones":
                        print("🎉 Ang husay mo! Isa pa!\n")
                        print("📜 Dalawang balon, hindi malingon. Ano ito?")
                        ans4 = input("Sagot mo: ").lower()

                        if ans4 == "mata":
                            print("🎉 Ang talino mo! Huling bugtong!\n")
                            print("📜 May puno, walang bunga; may dahon, walang sanga. Ano ito?")
                            ans5 = input("Sagot mo: ").lower()

                            if ans5 == "aklat":
                                print("🎉🎉🎉 Binabati kita! Natapos mo ang laro! 🏆")
                                break  
                            else:
                                print("❌ Mali!")
                        else:
                            print("❌ Mali!")
                    else:
                        print("❌ Mali!")
                else:
                    print("❌ Mali!")
            else:
                print("❌ Mali!")

            retry = input("❓ Gusto mo bang subukang muli? (oo/hindi): ").lower()
            if retry != "oo":
                print("😢 Salamat sa paglalaro! Paalam!")
                exit()  

    elif start == "hindi":
        print("😢 Sayang! Balik ka kapag gusto mo na maglaro.")
        break  
    else:
        print("❌ Hindi ko naintindihan ang sagot mo. Pakisubukang muli.")
