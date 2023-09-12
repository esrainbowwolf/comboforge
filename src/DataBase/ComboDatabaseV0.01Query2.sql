CREATE TABLE Rating_Adjustments(
AdjustmentID int NOT NULL AUTO_INCREMENT,
ComboID INT FOREIGN KEY REFERENCES Combos(ComboID),
Reply LONGTEXT,
Anonymous BOOL,
Username VARCHAR(255) FOREIGN KEY REFERENCES Users(Username),
Rating INT,
Amber_Creation INT,
Amber_Control INT,
Creature_Control INT,
Efficiency INT,
Make_Key bool,
PRIMARY KEY (AdjustmentID)
);