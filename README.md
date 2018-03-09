# PyConFireman

## Čo je PyConFireman?

Slovo "Fireman" v preklade do slovenčiny znamená hasič. Teda PyConFireman je hasič, ktorý prišiel hasiť búrlivý oheň na PyCon. V princípe funguje veľmi jednoducho, zapáliš zapalovač a on ti ho uhasí. Je to projekt, ktorý bol vyvinutý aby bol jednoduchý, ale aj zaujímavý. Tento projekt je taktiež veľmi jednoducho zreplikovateľný, čiže si ho nemusím užívať iba ja, ale kľudne si ho môžeš užívať aj ty.

## Hasí reálne oheň?


Áno, treba si dávať bacha. Prípadne odporúčam spraviť ho celého z nejakého kovu, aby nebol horľavý ako ten môj :P
## Z Čoho sa skladá PyConFireman?

Projekt je relatívne lacný, všetko sa dá zohnať pod 15 Eur.

### Senzor Plameňa

**Cena**: 0,50 * 7 = 3,50 Eur

**Zapojenie**: 

**Ako funguje**: Senzor Plameňa ti vie dať dva typy výstupov - analogový alebo digitálny. Analogový výstup ti povie intenzitu žiarenia plameňa. Avšak ovládacia jednotka NodeMCU má iba jeden analogový port, čiže by sme nevedeli monitorovať všetkých 7 senzorov. Zostáva nám teda iba digitálny vstup, ktorý nám povie iba to, či plameň vidí, alebo nevidí. Hranicu medzi videním a nevidením plameňa vieme nastaviť pomocou skrutkovača. Tým, že monitorujeme digitálny výstup senzora, zapojíme pin DO do akéhokoľvek digitálneho pina na NodeMCU. Senzor napájame do pinu VCC na 3,3V čo je maximálna tolerancia pre NodeMCU na digitálne vstupy. GND uzemníme.

### 180° Servo

**Cena**: 1,50 Eur

**Zapojenie**:

**Ako funguje**: Servo potrebuje na napájanie 5V, ktoré (kým napájaš NodeMCU z USB portu) nájdeš na pine Vin. Najtmavší (väčšinou hnedý) kábel uzemníš. Servo sa ovláda cez PWM, teda cez Impulzovú šírkovú moduláciu. Zjednodušene je to rýchle zapínanie a vypínanie určitého pinu v určitej frekvencii. Servo monitoruje túto frekvenciu a podľa nej sa otočí od 0° do 180°, teda najsvetlejší pin zapojíme do akéhokoľvek digitálneho pinu. 

### Ventilátor + NPN Tranzistor

**Cena**: 5 + 0,5 = 5,50 Eur

**Zapojenie**:

**Ako funguje**: Ventilátor je normálny DC motor. Keď mu zapojíme + na + a - na -, tak sa bude točiť. Tým, že chceme regulovať, či je ventilátor vypnutý alebo zapnutý, musíme použiť tranzistor (môžeme použiť aj relátko). Tranzistor zjednodušene funguje ako elektronický gombík. Iba namiesto mechanickej sily používa na spínanie prúdu elektrický náboj. Teda keď mu pustíme do jednej z troch nožiek prúd, tak zopne ďalšie dve.
