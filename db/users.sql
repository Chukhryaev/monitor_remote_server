CREATE TABLE IF NOT EXISTS `billdb`.`users` (
  `SKEY` INT NOT NULL AUTO_INCREMENT,
  `GUID` CHAR(32) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `name` VARCHAR(120) NULL,
  `password` CHAR(256) NOT NULL,
  `status` TINYINT NOT NULL DEFAULT -100 COMMENT '-100 Banned\n-50 Unactive\n0 Active\n',
  `role` TINYINT NOT NULL DEFAULT 0 COMMENT '0 No permission\n1 User\n5 Moderator\n10 Admin',
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`SKEY`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB