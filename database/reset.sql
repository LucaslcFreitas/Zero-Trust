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

DELETE FROM "zt-ehealth"."Permissao";

INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 1, 'Leitura', '2023-05-24 09:42:22.523995-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 2, 'Leitura', '2023-05-24 09:44:09.894398-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 2, 'Escrita', '2023-05-24 09:44:09.894398-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 2, 'Modificacao', '2023-05-24 09:44:09.894398-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 2, 'Exclusao', '2023-05-24 09:44:09.894398-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 3, 'Leitura', '2023-05-24 09:45:26.116141-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 3, 'Escrita', '2023-05-24 09:45:26.116141-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 3, 'Modificacao', '2023-05-24 09:45:26.116141-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 3, 'Exclusao', '2023-05-24 09:45:26.116141-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 4, 'Leitura', '2023-05-24 09:46:39.281641-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 4, 'Escrita', '2023-05-24 09:46:39.281641-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 4, 'Modificacao', '2023-05-24 09:46:39.281641-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 4, 'Exclusao', '2023-05-24 09:46:39.281641-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 5, 'Leitura', '2023-05-24 09:47:36.712956-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 5, 'Escrita', '2023-05-24 09:47:36.712956-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 5, 'Modificacao', '2023-05-24 09:47:36.712956-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 5, 'Exclusao', '2023-05-24 09:47:36.712956-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 6, 'Leitura', '2023-05-24 09:49:22.820335-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 6, 'Escrita', '2023-05-24 09:49:22.820335-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 6, 'Modificacao', '2023-05-24 09:49:22.820335-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 7, 'Leitura', '2023-05-24 09:50:16.313149-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 8, 'Leitura', '2023-05-24 09:50:54.077633-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 8, 'Escrita', '2023-05-24 09:50:54.077633-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 8, 'Modificacao', '2023-05-24 09:50:54.077633-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 8, 'Exclusao', '2023-05-24 09:50:54.077633-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 9, 'Leitura', '2023-05-24 09:53:05.519369-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 10, 'Leitura', '2023-05-24 09:53:41.119501-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 11, 'Leitura', '2023-05-24 09:54:26.269277-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 11, 'Escrita', '2023-05-24 09:54:26.269277-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 11, 'Modificacao', '2023-05-24 09:54:26.269277-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 11, 'Exclusao', '2023-05-24 09:54:26.269277-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 14, 'Leitura', '2023-05-24 09:55:22.541239-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 15, 'Leitura', '2023-05-24 09:56:15.118516-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 16, 'Leitura', '2023-05-24 09:57:19.483106-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 18, 'Leitura', '2023-05-24 09:58:10.641345-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 19, 'Leitura', '2023-05-24 09:58:40.640382-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 20, 'Leitura', '2023-05-24 09:59:19.420575-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 20, 'Escrita', '2023-05-24 09:59:19.420575-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 20, 'Modificacao', '2023-05-24 09:59:19.420575-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 20, 'Exclusao', '2023-05-24 09:59:19.420575-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 23, 'Leitura', '2023-05-24 10:02:54.956769-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 24, 'Leitura', '2023-05-24 10:04:04.705691-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 25, 'Leitura', '2023-05-24 10:04:47.102023-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 25, 'Escrita', '2023-05-24 10:04:47.102023-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 25, 'Exclusao', '2023-05-24 10:04:47.102023-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (1, 26, 'Acesso', '2023-05-24 10:06:01.493265-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 1, 'Leitura', '2023-05-24 10:14:53.22344-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 2, 'Leitura', '2023-05-24 10:15:24.449359-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 2, 'Escrita', '2023-05-24 10:15:24.449359-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 2, 'Modificacao', '2023-05-24 10:15:24.449359-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 2, 'Exclusao', '2023-05-24 10:15:24.449359-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 3, 'Leitura', '2023-05-24 10:16:19.458837-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 3, 'Escrita', '2023-05-24 10:16:19.458837-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 3, 'Modificacao', '2023-05-24 10:16:19.458837-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 3, 'Exclusao', '2023-05-24 10:16:19.458837-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 4, 'Leitura', '2023-05-24 10:17:16.21039-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 4, 'Escrita', '2023-05-24 10:17:16.21039-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 4, 'Modificacao', '2023-05-24 10:17:16.21039-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 4, 'Exclusao', '2023-05-24 10:17:16.21039-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 5, 'Leitura', '2023-05-24 10:18:29.088346-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 5, 'Escrita', '2023-05-24 10:18:29.088346-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 5, 'Modificacao', '2023-05-24 10:18:29.088346-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 5, 'Exclusao', '2023-05-24 10:18:29.088346-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 6, 'Leitura', '2023-05-24 10:19:32.835518-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 6, 'Escrita', '2023-05-24 10:19:32.835518-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 6, 'Modificacao', '2023-05-24 10:19:32.835518-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 7, 'Leitura', '2023-05-24 10:20:24.459465-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 8, 'Leitura', '2023-05-24 10:22:31.571458-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 8, 'Escrita', '2023-05-24 10:22:31.571458-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 8, 'Modificacao', '2023-05-24 10:22:31.571458-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 8, 'Exclusao', '2023-05-24 10:22:31.571458-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 9, 'Leitura', '2023-05-24 10:23:24.062783-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 10, 'Leitura', '2023-05-24 10:23:59.834716-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 11, 'Leitura', '2023-05-24 10:24:32.581292-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 11, 'Escrita', '2023-05-24 10:24:32.581292-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 11, 'Modificacao', '2023-05-24 10:24:32.581292-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 11, 'Exclusao', '2023-05-24 10:24:32.581292-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 14, 'Leitura', '2023-05-24 10:25:42.849148-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 15, 'Leitura', '2023-05-24 10:26:31.595973-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 16, 'Leitura', '2023-05-24 10:27:05.084695-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 18, 'Leitura', '2023-05-24 10:27:39.024299-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 19, 'Leitura', '2023-05-24 10:28:04.233126-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 20, 'Leitura', '2023-05-24 10:28:42.675885-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 20, 'Escrita', '2023-05-24 10:28:42.675885-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 20, 'Modificacao', '2023-05-24 10:28:42.675885-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 20, 'Exclusao', '2023-05-24 10:28:42.675885-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 23, 'Leitura', '2023-05-24 10:29:55.700224-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 24, 'Leitura', '2023-05-24 10:30:31.738012-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 25, 'Leitura', '2023-05-24 10:31:01.961341-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 25, 'Escrita', '2023-05-24 10:31:01.961341-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 25, 'Exclusao', '2023-05-24 10:31:01.961341-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (2, 26, 'Acesso', '2023-05-24 10:31:51.581223-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 1, 'Leitura', '2023-05-24 10:32:57.876515-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 2, 'Leitura', '2023-05-24 10:34:28.906775-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 3, 'Leitura', '2023-05-24 10:35:23.724742-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 3, 'Escrita', '2023-05-24 10:35:23.724742-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 3, 'Modificacao', '2023-05-24 10:35:23.724742-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 3, 'Exclusao', '2023-05-24 10:35:23.724742-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 5, 'Leitura', '2023-05-24 10:39:44.561347-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 7, 'Leitura', '2023-05-24 10:40:20.242879-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 8, 'Leitura', '2023-05-24 10:41:58.838373-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 9, 'Leitura', '2023-05-24 10:42:40.428267-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 10, 'Leitura', '2023-05-24 10:45:28.409437-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 11, 'Leitura', '2023-05-24 10:46:37.215794-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 14, 'Leitura', '2023-05-24 10:47:06.81154-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 15, 'Leitura', '2023-05-24 10:55:15.957319-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 16, 'Leitura', '2023-05-24 10:55:56.066439-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 19, 'Leitura', '2023-05-24 10:56:56.767223-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 20, 'Leitura', '2023-05-24 10:58:10.268207-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 23, 'Leitura', '2023-05-24 10:58:47.336147-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (3, 24, 'Leitura', '2023-05-24 10:59:38.945141-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 1, 'Leitura', '2023-05-24 11:07:10.879409-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 1, 'Escrita', '2023-05-24 11:07:10.879409-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 1, 'Modificacao', '2023-05-24 11:07:10.879409-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 7, 'Leitura', '2023-05-24 11:08:43.321395-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 9, 'Leitura', '2023-05-24 11:09:17.615391-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 9, 'Escrita', '2023-05-24 11:09:17.615391-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 9, 'Modificacao', '2023-05-24 11:09:17.615391-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 11, 'Leitura', '2023-05-24 11:10:16.861504-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 12, 'Leitura', '2023-05-24 11:10:59.208254-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 12, 'Escrita', '2023-05-24 11:10:59.208254-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 12, 'Modificacao', '2023-05-24 11:10:59.208254-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 21, 'Leitura', '2023-05-24 11:17:00.508929-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 22, 'Leitura', '2023-05-24 11:17:32.270578-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 22, 'Escrita', '2023-05-24 11:17:32.270578-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 22, 'Modificacao', '2023-05-24 11:17:32.270578-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 22, 'Exclusao', '2023-05-24 11:17:32.270578-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (4, 23, 'Leitura', '2023-05-24 11:19:35.09776-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 10, 'Leitura', '2023-05-24 11:32:56.116302-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 10, 'Escrita', '2023-05-24 11:32:56.116302-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 10, 'Modificacao', '2023-05-24 11:32:56.116302-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 10, 'Exclusao', '2023-05-24 11:32:56.116302-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 12, 'Leitura', '2023-05-24 11:34:06.426901-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 12, 'Escrita', '2023-05-24 11:34:06.426901-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 12, 'Modificacao', '2023-05-24 11:34:06.426901-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 12, 'Exclusao', '2023-05-24 11:34:06.426901-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 13, 'Leitura', '2023-05-24 11:35:14.588553-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 13, 'Escrita', '2023-05-24 11:35:14.588553-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 13, 'Modificacao', '2023-05-24 11:35:14.588553-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 13, 'Exclusao', '2023-05-24 11:35:14.588553-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 14, 'Leitura', '2023-05-24 11:36:37.086521-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 14, 'Escrita', '2023-05-24 11:36:37.086521-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 14, 'Modificacao', '2023-05-24 11:36:37.086521-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (5, 14, 'Exclusao', '2023-05-24 11:36:37.086521-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 15, 'Leitura', '2023-05-24 11:39:58.211156-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 16, 'Leitura', '2023-05-24 11:40:19.467267-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 18, 'Leitura', '2023-05-24 11:40:40.355389-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 19, 'Leitura', '2023-05-24 11:42:14.584492-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 19, 'Modificacao', '2023-05-24 11:42:14.584492-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 20, 'Leitura', '2023-05-24 11:42:54.813301-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 21, 'Leitura', '2023-05-24 11:43:54.969993-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 22, 'Leitura', '2023-05-24 11:44:30.875866-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 22, 'Escrita', '2023-05-24 11:44:30.875866-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 23, 'Leitura', '2023-05-24 11:45:18.756764-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 23, 'Escrita', '2023-05-24 11:45:18.756764-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 24, 'Leitura', '2023-05-24 11:46:00.181497-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 24, 'Modificacao', '2023-05-24 11:46:00.181497-03', 'Ativo');
INSERT INTO "zt-ehealth"."Permissao" ("idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status) VALUES (6, 26, 'Acesso', '2023-05-24 11:46:41.699374-03', 'Ativo');
