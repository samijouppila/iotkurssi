from serial import Serial
from enum import Enum
import time

class tila(Enum):
    alkuTila = 0
    suljettuEiLukossa = 1
    avoinnaEiLukossa = 2
    suljettuLukossa = 3
    avoinnaLukossa = 4
    
mTila = tila.alkuTila
mEdellinenTila = tila.alkuTila

toiminto = 'X'
    
   
mTila = tila.suljettuEiLukossa
mEdellinenTila = tila.alkuTila
    
def tulostaValikko():
    
    print("Valitse toiminto:\n")
    print("O tai o (open) = Avaa ovi\n")
    print("C tai c (close) = Sulje ovi\n")
    print("L tai l (lock) = Lukitse ovi\n")
    print("U tai u (Unlock) = Aukaise lukko\n")
## -----
    
def lueValinta():
    merkki  = input()
    merkki.upper()
    
    print(merkki)
    
    
    if merkki == 'O' or 'C' or 'L' or 'U':
        return merkki
    else:
        return 'X'
    

def suljettuEiLukossaEntryToiminnot():
    print("Entry SuljettuEiLukossa-tila\n")
## ---

def suljettuEiLukossaExitToiminnot():
    print("Exit SuljettuEiLukossa-tila\n")
## ---
    
def avoinnaEiLukossaDoToiminnot():
    print("Do AvoinnaEiLukossa-tila\n")
## ---
    
def suljettuLukossaEntryToiminnot():
    print("Entry SuljettuLukossa-tila\n")
## ---
    

    
    



while 1:
    print(mTila)

    toiminto = lueValinta()
    
    if mTila == tila.suljettuEiLukossa:
        
        if not mEdellinenTila == mTila:
            suljettuEiLukossaEntryToiminnot()
        
        mEdellinenTila = mTila
        
        if toiminto == 'O':
            suljettuEiLukossaExitToiminnot()
            mTila = tila.avoinnaEiLukossa
            
        if toiminto == 'L':
            suljettuEiLukossaExitToiminnot()
            mTila = tila.suljettuLukossa
            
        
    elif mTila == tila.avoinnaEiLukossa:
        
        mEdellinenTila = mTila
        avoinnaEiLukossaDoToiminnot()
        
        if toiminto == 'C':
            mTila = tila.suljettuEiLukossa
        
    elif mTila == tila.suljettuLukossa:
        
        if not mEdellinenTila == mTila:
            suljettuLukossaEntryToiminnot()
            
        mEdellinenTila = mTila
        
        if toiminto == 'U':
            mTila = tila.suljettuEiLukossa
        
    elif mTila == tila.avoinnaLukossa:
        pass
        
            
    
    
    
    pass