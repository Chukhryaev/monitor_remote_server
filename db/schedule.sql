CREATE TABLE IF NOT EXISTS `billdb`.`Schedule` (
  `SKEY` INT NOT NULL AUTO_INCREMENT,
  `GUID` VARCHAR(32) NULL,
  `body` VARCHAR(65536) NULL,
  `date` DATE NOT NULL,
  `Monitors_SKEY` INT NOT NULL,
  PRIMARY KEY (`SKEY`, `Monitors_SKEY`),
  INDEX `fk_Schedule_Monitors1_idx` (`Monitors_SKEY` ASC) VISIBLE,
  CONSTRAINT `fk_Schedule_Monitors1`
    FOREIGN KEY (`Monitors_SKEY`)
    REFERENCES `andrew_test`.`Monitors` (`SKEY`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB