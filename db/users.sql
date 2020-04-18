CREATE TABLE IF NOT EXISTS `billdb`.`users` (
  `SKEY` INT(11) NOT NULL AUTO_INCREMENT,
  `GUID` CHAR(32) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `name` VARCHAR(120) NULL DEFAULT NULL,
  `password` CHAR(255) NOT NULL,
  `status` TINYINT(4) NOT NULL DEFAULT '-100' COMMENT '-100 Banned\\n-50 Unactive\\n0 Active\\n',
  `role` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '0 No permission\\n1 User\\n5 Moderator\\n10 Admin',
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`SKEY`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1