DELETE FROM "zt-ehealth"."Acesso";

DELETE FROM "zt-ehealth"."CaracteristicaDispositivo";

DELETE FROM "zt-ehealth"."Dispositivo";

DELETE FROM "zt-ehealth"."DispositivoTMP";

DELETE FROM "zt-ehealth"."Token";

DELETE FROM "zt-ehealth"."RegLogin";

DELETE FROM "zt-ehealth"."Senha";
INSERT INTO "zt-ehealth"."Senha"(
	"idUsuario", senha, "dataCriacao", status)
	VALUES (1, 'cf6d058dedf9a66c5b039cec186022aab3f33d7bdd19112f07ed44e513d326fe', '2023-05-23 11:20:08.369516-03', 'Ativo');
INSERT INTO "zt-ehealth"."Senha"(
	"idUsuario", senha, "dataCriacao", status)
	VALUES (2, '0e3eb10df8dd1509b3f86c07974f3681f2fee0d603b5ad58c4e3374302804094', '2023-05-23 11:22:02.776633-03', 'Ativo');
INSERT INTO "zt-ehealth"."Senha"(
	"idUsuario", senha, "dataCriacao", status)
	VALUES (3, '28646fceb3510a46df7b489c7e994b14ab546809ca6e9e4945ccfbd0962e41bd', '2023-05-23 11:22:48.612575-03', 'Ativo');
INSERT INTO "zt-ehealth"."Senha"(
	"idUsuario", senha, "dataCriacao", status)
	VALUES (4, 'e15719bc1fd4d59cacc6a6dd7e1dc7779b80d48cd3fe38692f6f4ca395ff7223', '2023-05-23 11:23:31.749759-03', 'Ativo');
INSERT INTO "zt-ehealth"."Senha"(
	"idUsuario", senha, "dataCriacao", status)
	VALUES (5, 'd5ae99cacd4c196c87bf3fafeecb1a72f7cfcfd3834292b2a41e2fcd2520903e', '2023-05-23 11:24:48.398614-03', 'Ativo');
INSERT INTO "zt-ehealth"."Senha"(
	"idUsuario", senha, "dataCriacao", status)
	VALUES (6, '72863cd1a78bf14f433d6473930a60d21789b1c7655137dce2857f16ae5093e4', '2023-05-23 11:25:20.549288-03', 'Ativo');