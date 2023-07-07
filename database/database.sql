PGDMP                         {         
   zt-ehealth    15.3    15.3 ~    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398 
   zt-ehealth    DATABASE     �   CREATE DATABASE "zt-ehealth" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "zt-ehealth";
                postgres    false                        2615    16399 
   zt-ehealth    SCHEMA        CREATE SCHEMA "zt-ehealth";
    DROP SCHEMA "zt-ehealth";
                postgres    false            �            1259    16576    Acesso    TABLE     D  CREATE TABLE "zt-ehealth"."Acesso" (
    id integer NOT NULL,
    "idUsuario" integer,
    "idToken" integer,
    "idPermissao" integer,
    "idSubRecurso" integer NOT NULL,
    "idSensibilidadeSubRecurso" integer NOT NULL,
    "idDispositivo" integer,
    latitude character varying(16) NOT NULL,
    longitude character varying(16) NOT NULL,
    data timestamp with time zone NOT NULL,
    resultado character varying(16) NOT NULL,
    rede character varying(16) NOT NULL,
    confianca real NOT NULL,
    "idDispositivoTMP" integer,
    reautenticacao boolean DEFAULT false
);
 "   DROP TABLE "zt-ehealth"."Acesso";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16575    Acesso_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Acesso_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE "zt-ehealth"."Acesso_id_seq";
    
   zt-ehealth          postgres    false    236    6            �           0    0    Acesso_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE "zt-ehealth"."Acesso_id_seq" OWNED BY "zt-ehealth"."Acesso".id;
       
   zt-ehealth          postgres    false    235            �            1259    16663    CaracteristicaDispositivo    TABLE     m  CREATE TABLE "zt-ehealth"."CaracteristicaDispositivo" (
    id integer NOT NULL,
    "deviceFingerPrint" character varying(256) NOT NULL,
    "sistemaOperacional" character varying(50) NOT NULL,
    "versaoSO" character varying NOT NULL,
    data timestamp with time zone NOT NULL,
    status character varying(10) NOT NULL,
    "idDispositivo" integer NOT NULL
);
 5   DROP TABLE "zt-ehealth"."CaracteristicaDispositivo";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16662     CaracteristicaDispositivo_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."CaracteristicaDispositivo_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE "zt-ehealth"."CaracteristicaDispositivo_id_seq";
    
   zt-ehealth          postgres    false    6    240            �           0    0     CaracteristicaDispositivo_id_seq    SEQUENCE OWNED BY     u   ALTER SEQUENCE "zt-ehealth"."CaracteristicaDispositivo_id_seq" OWNED BY "zt-ehealth"."CaracteristicaDispositivo".id;
       
   zt-ehealth          postgres    false    239            �            1259    16468    Cliente    TABLE     c   CREATE TABLE "zt-ehealth"."Cliente" (
    id integer NOT NULL,
    "idUsuario" integer NOT NULL
);
 #   DROP TABLE "zt-ehealth"."Cliente";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16537    Dispositivo    TABLE     o   CREATE TABLE "zt-ehealth"."Dispositivo" (
    id integer NOT NULL,
    "MAC" character varying(18) NOT NULL
);
 '   DROP TABLE "zt-ehealth"."Dispositivo";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16677    DispositivoTMP    TABLE     6  CREATE TABLE "zt-ehealth"."DispositivoTMP" (
    id integer NOT NULL,
    "MAC" character varying(18) NOT NULL,
    "deviceFingerPrint" character varying(256) NOT NULL,
    "SistemaOperacional" character varying(50) NOT NULL,
    "versaoSO" character varying NOT NULL,
    data time with time zone NOT NULL
);
 *   DROP TABLE "zt-ehealth"."DispositivoTMP";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16676    DispositivoTMP_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."DispositivoTMP_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE "zt-ehealth"."DispositivoTMP_id_seq";
    
   zt-ehealth          postgres    false    6    242            �           0    0    DispositivoTMP_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE "zt-ehealth"."DispositivoTMP_id_seq" OWNED BY "zt-ehealth"."DispositivoTMP".id;
       
   zt-ehealth          postgres    false    241            �            1259    16536    Dispositivo_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Dispositivo_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE "zt-ehealth"."Dispositivo_id_seq";
    
   zt-ehealth          postgres    false    230    6            �           0    0    Dispositivo_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE "zt-ehealth"."Dispositivo_id_seq" OWNED BY "zt-ehealth"."Dispositivo".id;
       
   zt-ehealth          postgres    false    229            �            1259    16467    Paciente_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Paciente_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE "zt-ehealth"."Paciente_id_seq";
    
   zt-ehealth          postgres    false    6    222            �           0    0    Paciente_id_seq    SEQUENCE OWNED BY     R   ALTER SEQUENCE "zt-ehealth"."Paciente_id_seq" OWNED BY "zt-ehealth"."Cliente".id;
       
   zt-ehealth          postgres    false    221            �            1259    16518 	   Permissao    TABLE     Z  CREATE TABLE "zt-ehealth"."Permissao" (
    id integer NOT NULL,
    "idUsuario" integer,
    "idSubRecurso" integer NOT NULL,
    "tipoAcao" character varying(13) NOT NULL,
    "dataCriacao" timestamp with time zone NOT NULL,
    status character varying(10) NOT NULL,
    "dataExclusao" timestamp with time zone,
    "idDispositivo" integer
);
 %   DROP TABLE "zt-ehealth"."Permissao";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16517    Permissao_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Permissao_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE "zt-ehealth"."Permissao_id_seq";
    
   zt-ehealth          postgres    false    228    6            �           0    0    Permissao_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE "zt-ehealth"."Permissao_id_seq" OWNED BY "zt-ehealth"."Permissao".id;
       
   zt-ehealth          postgres    false    227            �            1259    16413    Profissional    TABLE     >  CREATE TABLE "zt-ehealth"."Profissional" (
    id integer NOT NULL,
    cargo character varying(50) NOT NULL,
    "diasTrabalho" character varying(50) NOT NULL,
    "idUsuario" integer NOT NULL,
    "horarioTrabalhoInicio" time without time zone NOT NULL,
    "horarioTrabalhoFinal" time without time zone NOT NULL
);
 (   DROP TABLE "zt-ehealth"."Profissional";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16412    Profissional_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Profissional_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE "zt-ehealth"."Profissional_id_seq";
    
   zt-ehealth          postgres    false    6    218            �           0    0    Profissional_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE "zt-ehealth"."Profissional_id_seq" OWNED BY "zt-ehealth"."Profissional".id;
       
   zt-ehealth          postgres    false    217            �            1259    16437    Recurso    TABLE     �   CREATE TABLE "zt-ehealth"."Recurso" (
    id integer NOT NULL,
    nome character varying(150) NOT NULL,
    "ipAddress" character varying(16) NOT NULL,
    porta integer NOT NULL
);
 #   DROP TABLE "zt-ehealth"."Recurso";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16436    Recurso_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Recurso_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE "zt-ehealth"."Recurso_id_seq";
    
   zt-ehealth          postgres    false    6    220            �           0    0    Recurso_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE "zt-ehealth"."Recurso_id_seq" OWNED BY "zt-ehealth"."Recurso".id;
       
   zt-ehealth          postgres    false    219            �            1259    16545    RegLogin    TABLE     	  CREATE TABLE "zt-ehealth"."RegLogin" (
    id integer NOT NULL,
    "idUsuario" integer,
    data timestamp with time zone NOT NULL,
    resultado character varying(10) NOT NULL,
    "idSenha" integer,
    "idDispositivo" integer,
    tipo character varying(15)
);
 $   DROP TABLE "zt-ehealth"."RegLogin";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16544    RegLogin_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."RegLogin_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE "zt-ehealth"."RegLogin_id_seq";
    
   zt-ehealth          postgres    false    6    232            �           0    0    RegLogin_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE "zt-ehealth"."RegLogin_id_seq" OWNED BY "zt-ehealth"."RegLogin".id;
       
   zt-ehealth          postgres    false    231            �            1259    16619    Senha    TABLE     �   CREATE TABLE "zt-ehealth"."Senha" (
    id integer NOT NULL,
    "idUsuario" integer NOT NULL,
    senha character varying(256) NOT NULL,
    "dataCriacao" timestamp with time zone NOT NULL,
    status character varying(12) NOT NULL
);
 !   DROP TABLE "zt-ehealth"."Senha";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16618    Senha_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Senha_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE "zt-ehealth"."Senha_id_seq";
    
   zt-ehealth          postgres    false    238    6            �           0    0    Senha_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE "zt-ehealth"."Senha_id_seq" OWNED BY "zt-ehealth"."Senha".id;
       
   zt-ehealth          postgres    false    237            �            1259    16504    SensibilidadeSubRecurso    TABLE     �   CREATE TABLE "zt-ehealth"."SensibilidadeSubRecurso" (
    id integer NOT NULL,
    "idSubRecurso" integer NOT NULL,
    "tipoAcao" character varying(12) NOT NULL,
    sensibilidade real NOT NULL
);
 3   DROP TABLE "zt-ehealth"."SensibilidadeSubRecurso";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16503    SensibilidadeSubRecurso_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."SensibilidadeSubRecurso_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 =   DROP SEQUENCE "zt-ehealth"."SensibilidadeSubRecurso_id_seq";
    
   zt-ehealth          postgres    false    6    226            �           0    0    SensibilidadeSubRecurso_id_seq    SEQUENCE OWNED BY     q   ALTER SEQUENCE "zt-ehealth"."SensibilidadeSubRecurso_id_seq" OWNED BY "zt-ehealth"."SensibilidadeSubRecurso".id;
       
   zt-ehealth          postgres    false    225            �            1259    16492 
   SubRecurso    TABLE     �   CREATE TABLE "zt-ehealth"."SubRecurso" (
    id integer NOT NULL,
    "idRecurso" integer NOT NULL,
    nome character varying(150) NOT NULL
);
 &   DROP TABLE "zt-ehealth"."SubRecurso";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16491    SubRecurso_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."SubRecurso_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE "zt-ehealth"."SubRecurso_id_seq";
    
   zt-ehealth          postgres    false    224    6            �           0    0    SubRecurso_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE "zt-ehealth"."SubRecurso_id_seq" OWNED BY "zt-ehealth"."SubRecurso".id;
       
   zt-ehealth          postgres    false    223            �            1259    16557    Token    TABLE     =  CREATE TABLE "zt-ehealth"."Token" (
    id integer NOT NULL,
    "idUsuario" integer,
    "idRegLogin" integer NOT NULL,
    hash character varying(256) NOT NULL,
    validade timestamp with time zone NOT NULL,
    status character varying(10) NOT NULL,
    "idDispositivo" integer,
    tipo character varying(15)
);
 !   DROP TABLE "zt-ehealth"."Token";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16556    Token_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Token_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE "zt-ehealth"."Token_id_seq";
    
   zt-ehealth          postgres    false    234    6            �           0    0    Token_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE "zt-ehealth"."Token_id_seq" OWNED BY "zt-ehealth"."Token".id;
       
   zt-ehealth          postgres    false    233            �            1259    16406    Usuario    TABLE     �   CREATE TABLE "zt-ehealth"."Usuario" (
    id integer NOT NULL,
    nome character varying(150) NOT NULL,
    tipo character varying(15) NOT NULL,
    cpf character varying(15) NOT NULL
);
 #   DROP TABLE "zt-ehealth"."Usuario";
    
   zt-ehealth         heap    postgres    false    6            �            1259    16405    Usuario_id_seq    SEQUENCE     �   CREATE SEQUENCE "zt-ehealth"."Usuario_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE "zt-ehealth"."Usuario_id_seq";
    
   zt-ehealth          postgres    false    216    6            �           0    0    Usuario_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE "zt-ehealth"."Usuario_id_seq" OWNED BY "zt-ehealth"."Usuario".id;
       
   zt-ehealth          postgres    false    215            �           2604    16579 	   Acesso id    DEFAULT     v   ALTER TABLE ONLY "zt-ehealth"."Acesso" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Acesso_id_seq"'::regclass);
 @   ALTER TABLE "zt-ehealth"."Acesso" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    235    236    236            �           2604    16666    CaracteristicaDispositivo id    DEFAULT     �   ALTER TABLE ONLY "zt-ehealth"."CaracteristicaDispositivo" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."CaracteristicaDispositivo_id_seq"'::regclass);
 S   ALTER TABLE "zt-ehealth"."CaracteristicaDispositivo" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    240    239    240            �           2604    16471 
   Cliente id    DEFAULT     y   ALTER TABLE ONLY "zt-ehealth"."Cliente" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Paciente_id_seq"'::regclass);
 A   ALTER TABLE "zt-ehealth"."Cliente" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    221    222    222            �           2604    16540    Dispositivo id    DEFAULT     �   ALTER TABLE ONLY "zt-ehealth"."Dispositivo" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Dispositivo_id_seq"'::regclass);
 E   ALTER TABLE "zt-ehealth"."Dispositivo" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    229    230    230            �           2604    16680    DispositivoTMP id    DEFAULT     �   ALTER TABLE ONLY "zt-ehealth"."DispositivoTMP" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."DispositivoTMP_id_seq"'::regclass);
 H   ALTER TABLE "zt-ehealth"."DispositivoTMP" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    241    242    242            �           2604    16521    Permissao id    DEFAULT     |   ALTER TABLE ONLY "zt-ehealth"."Permissao" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Permissao_id_seq"'::regclass);
 C   ALTER TABLE "zt-ehealth"."Permissao" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    228    227    228            �           2604    16416    Profissional id    DEFAULT     �   ALTER TABLE ONLY "zt-ehealth"."Profissional" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Profissional_id_seq"'::regclass);
 F   ALTER TABLE "zt-ehealth"."Profissional" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    218    217    218            �           2604    16440 
   Recurso id    DEFAULT     x   ALTER TABLE ONLY "zt-ehealth"."Recurso" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Recurso_id_seq"'::regclass);
 A   ALTER TABLE "zt-ehealth"."Recurso" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    220    219    220            �           2604    16548    RegLogin id    DEFAULT     z   ALTER TABLE ONLY "zt-ehealth"."RegLogin" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."RegLogin_id_seq"'::regclass);
 B   ALTER TABLE "zt-ehealth"."RegLogin" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    232    231    232            �           2604    16622    Senha id    DEFAULT     t   ALTER TABLE ONLY "zt-ehealth"."Senha" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Senha_id_seq"'::regclass);
 ?   ALTER TABLE "zt-ehealth"."Senha" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    238    237    238            �           2604    16507    SensibilidadeSubRecurso id    DEFAULT     �   ALTER TABLE ONLY "zt-ehealth"."SensibilidadeSubRecurso" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."SensibilidadeSubRecurso_id_seq"'::regclass);
 Q   ALTER TABLE "zt-ehealth"."SensibilidadeSubRecurso" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    226    225    226            �           2604    16495    SubRecurso id    DEFAULT     ~   ALTER TABLE ONLY "zt-ehealth"."SubRecurso" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."SubRecurso_id_seq"'::regclass);
 D   ALTER TABLE "zt-ehealth"."SubRecurso" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    223    224    224            �           2604    16560    Token id    DEFAULT     t   ALTER TABLE ONLY "zt-ehealth"."Token" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Token_id_seq"'::regclass);
 ?   ALTER TABLE "zt-ehealth"."Token" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    233    234    234            �           2604    16409 
   Usuario id    DEFAULT     x   ALTER TABLE ONLY "zt-ehealth"."Usuario" ALTER COLUMN id SET DEFAULT nextval('"zt-ehealth"."Usuario_id_seq"'::regclass);
 A   ALTER TABLE "zt-ehealth"."Usuario" ALTER COLUMN id DROP DEFAULT;
    
   zt-ehealth          postgres    false    215    216    216            �          0    16576    Acesso 
   TABLE DATA           �   COPY "zt-ehealth"."Acesso" (id, "idUsuario", "idToken", "idPermissao", "idSubRecurso", "idSensibilidadeSubRecurso", "idDispositivo", latitude, longitude, data, resultado, rede, confianca, "idDispositivoTMP", reautenticacao) FROM stdin;
 
   zt-ehealth          postgres    false    236   �       �          0    16663    CaracteristicaDispositivo 
   TABLE DATA           �   COPY "zt-ehealth"."CaracteristicaDispositivo" (id, "deviceFingerPrint", "sistemaOperacional", "versaoSO", data, status, "idDispositivo") FROM stdin;
 
   zt-ehealth          postgres    false    240   6�       �          0    16468    Cliente 
   TABLE DATA           :   COPY "zt-ehealth"."Cliente" (id, "idUsuario") FROM stdin;
 
   zt-ehealth          postgres    false    222   S�       �          0    16537    Dispositivo 
   TABLE DATA           8   COPY "zt-ehealth"."Dispositivo" (id, "MAC") FROM stdin;
 
   zt-ehealth          postgres    false    230   t�       �          0    16677    DispositivoTMP 
   TABLE DATA           x   COPY "zt-ehealth"."DispositivoTMP" (id, "MAC", "deviceFingerPrint", "SistemaOperacional", "versaoSO", data) FROM stdin;
 
   zt-ehealth          postgres    false    242   ��       �          0    16518 	   Permissao 
   TABLE DATA           �   COPY "zt-ehealth"."Permissao" (id, "idUsuario", "idSubRecurso", "tipoAcao", "dataCriacao", status, "dataExclusao", "idDispositivo") FROM stdin;
 
   zt-ehealth          postgres    false    228   ��       |          0    16413    Profissional 
   TABLE DATA           �   COPY "zt-ehealth"."Profissional" (id, cargo, "diasTrabalho", "idUsuario", "horarioTrabalhoInicio", "horarioTrabalhoFinal") FROM stdin;
 
   zt-ehealth          postgres    false    218   %�       ~          0    16437    Recurso 
   TABLE DATA           G   COPY "zt-ehealth"."Recurso" (id, nome, "ipAddress", porta) FROM stdin;
 
   zt-ehealth          postgres    false    220   �       �          0    16545    RegLogin 
   TABLE DATA           n   COPY "zt-ehealth"."RegLogin" (id, "idUsuario", data, resultado, "idSenha", "idDispositivo", tipo) FROM stdin;
 
   zt-ehealth          postgres    false    232   ��       �          0    16619    Senha 
   TABLE DATA           V   COPY "zt-ehealth"."Senha" (id, "idUsuario", senha, "dataCriacao", status) FROM stdin;
 
   zt-ehealth          postgres    false    238   ��       �          0    16504    SensibilidadeSubRecurso 
   TABLE DATA           h   COPY "zt-ehealth"."SensibilidadeSubRecurso" (id, "idSubRecurso", "tipoAcao", sensibilidade) FROM stdin;
 
   zt-ehealth          postgres    false    226   �       �          0    16492 
   SubRecurso 
   TABLE DATA           C   COPY "zt-ehealth"."SubRecurso" (id, "idRecurso", nome) FROM stdin;
 
   zt-ehealth          postgres    false    224   M�       �          0    16557    Token 
   TABLE DATA           u   COPY "zt-ehealth"."Token" (id, "idUsuario", "idRegLogin", hash, validade, status, "idDispositivo", tipo) FROM stdin;
 
   zt-ehealth          postgres    false    234   е       z          0    16406    Usuario 
   TABLE DATA           >   COPY "zt-ehealth"."Usuario" (id, nome, tipo, cpf) FROM stdin;
 
   zt-ehealth          postgres    false    216   ��       �           0    0    Acesso_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('"zt-ehealth"."Acesso_id_seq"', 41492, true);
       
   zt-ehealth          postgres    false    235            �           0    0     CaracteristicaDispositivo_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('"zt-ehealth"."CaracteristicaDispositivo_id_seq"', 400, true);
       
   zt-ehealth          postgres    false    239            �           0    0    DispositivoTMP_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('"zt-ehealth"."DispositivoTMP_id_seq"', 14809, true);
       
   zt-ehealth          postgres    false    241            �           0    0    Dispositivo_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('"zt-ehealth"."Dispositivo_id_seq"', 391, true);
       
   zt-ehealth          postgres    false    229            �           0    0    Paciente_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('"zt-ehealth"."Paciente_id_seq"', 1, true);
       
   zt-ehealth          postgres    false    221            �           0    0    Permissao_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('"zt-ehealth"."Permissao_id_seq"', 958, true);
       
   zt-ehealth          postgres    false    227            �           0    0    Profissional_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('"zt-ehealth"."Profissional_id_seq"', 5, true);
       
   zt-ehealth          postgres    false    217            �           0    0    Recurso_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('"zt-ehealth"."Recurso_id_seq"', 5, true);
       
   zt-ehealth          postgres    false    219            �           0    0    RegLogin_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('"zt-ehealth"."RegLogin_id_seq"', 11485, true);
       
   zt-ehealth          postgres    false    231            �           0    0    Senha_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('"zt-ehealth"."Senha_id_seq"', 2008, true);
       
   zt-ehealth          postgres    false    237            �           0    0    SensibilidadeSubRecurso_id_seq    SEQUENCE SET     U   SELECT pg_catalog.setval('"zt-ehealth"."SensibilidadeSubRecurso_id_seq"', 94, true);
       
   zt-ehealth          postgres    false    225            �           0    0    SubRecurso_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('"zt-ehealth"."SubRecurso_id_seq"', 26, true);
       
   zt-ehealth          postgres    false    223            �           0    0    Token_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('"zt-ehealth"."Token_id_seq"', 11224, true);
       
   zt-ehealth          postgres    false    233            �           0    0    Usuario_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('"zt-ehealth"."Usuario_id_seq"', 6, true);
       
   zt-ehealth          postgres    false    215            �           2606    16583    Acesso Acesso_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_pkey" PRIMARY KEY (id);
 F   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_pkey";
    
   zt-ehealth            postgres    false    236            �           2606    16670 8   CaracteristicaDispositivo CaracteristicaDispositivo_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."CaracteristicaDispositivo"
    ADD CONSTRAINT "CaracteristicaDispositivo_pkey" PRIMARY KEY (id);
 l   ALTER TABLE ONLY "zt-ehealth"."CaracteristicaDispositivo" DROP CONSTRAINT "CaracteristicaDispositivo_pkey";
    
   zt-ehealth            postgres    false    240            �           2606    16684 "   DispositivoTMP DispositivoTMP_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY "zt-ehealth"."DispositivoTMP"
    ADD CONSTRAINT "DispositivoTMP_pkey" PRIMARY KEY (id);
 V   ALTER TABLE ONLY "zt-ehealth"."DispositivoTMP" DROP CONSTRAINT "DispositivoTMP_pkey";
    
   zt-ehealth            postgres    false    242            �           2606    16610    Dispositivo Dispositivo_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY "zt-ehealth"."Dispositivo"
    ADD CONSTRAINT "Dispositivo_pkey" PRIMARY KEY (id);
 P   ALTER TABLE ONLY "zt-ehealth"."Dispositivo" DROP CONSTRAINT "Dispositivo_pkey";
    
   zt-ehealth            postgres    false    230            �           2606    16473    Cliente Paciente_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY "zt-ehealth"."Cliente"
    ADD CONSTRAINT "Paciente_pkey" PRIMARY KEY (id);
 I   ALTER TABLE ONLY "zt-ehealth"."Cliente" DROP CONSTRAINT "Paciente_pkey";
    
   zt-ehealth            postgres    false    222            �           2606    16530    Permissao Permissao_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY "zt-ehealth"."Permissao"
    ADD CONSTRAINT "Permissao_pkey" PRIMARY KEY (id);
 L   ALTER TABLE ONLY "zt-ehealth"."Permissao" DROP CONSTRAINT "Permissao_pkey";
    
   zt-ehealth            postgres    false    228            �           2606    16418    Profissional Profissional_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY "zt-ehealth"."Profissional"
    ADD CONSTRAINT "Profissional_pkey" PRIMARY KEY (id);
 R   ALTER TABLE ONLY "zt-ehealth"."Profissional" DROP CONSTRAINT "Profissional_pkey";
    
   zt-ehealth            postgres    false    218            �           2606    16442    Recurso Recurso_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY "zt-ehealth"."Recurso"
    ADD CONSTRAINT "Recurso_pkey" PRIMARY KEY (id);
 H   ALTER TABLE ONLY "zt-ehealth"."Recurso" DROP CONSTRAINT "Recurso_pkey";
    
   zt-ehealth            postgres    false    220            �           2606    16550    RegLogin RegLogin_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY "zt-ehealth"."RegLogin"
    ADD CONSTRAINT "RegLogin_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY "zt-ehealth"."RegLogin" DROP CONSTRAINT "RegLogin_pkey";
    
   zt-ehealth            postgres    false    232            �           2606    16624    Senha Senha_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY "zt-ehealth"."Senha"
    ADD CONSTRAINT "Senha_pkey" PRIMARY KEY (id);
 D   ALTER TABLE ONLY "zt-ehealth"."Senha" DROP CONSTRAINT "Senha_pkey";
    
   zt-ehealth            postgres    false    238            �           2606    16516 4   SensibilidadeSubRecurso SensibilidadeSubRecurso_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY "zt-ehealth"."SensibilidadeSubRecurso"
    ADD CONSTRAINT "SensibilidadeSubRecurso_pkey" PRIMARY KEY (id);
 h   ALTER TABLE ONLY "zt-ehealth"."SensibilidadeSubRecurso" DROP CONSTRAINT "SensibilidadeSubRecurso_pkey";
    
   zt-ehealth            postgres    false    226            �           2606    16502    SubRecurso SubRecurso_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY "zt-ehealth"."SubRecurso"
    ADD CONSTRAINT "SubRecurso_pkey" PRIMARY KEY (id);
 N   ALTER TABLE ONLY "zt-ehealth"."SubRecurso" DROP CONSTRAINT "SubRecurso_pkey";
    
   zt-ehealth            postgres    false    224            �           2606    16617    Token Token_hash_key 
   CONSTRAINT     Y   ALTER TABLE ONLY "zt-ehealth"."Token"
    ADD CONSTRAINT "Token_hash_key" UNIQUE (hash);
 H   ALTER TABLE ONLY "zt-ehealth"."Token" DROP CONSTRAINT "Token_hash_key";
    
   zt-ehealth            postgres    false    234            �           2606    16569    Token Token_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY "zt-ehealth"."Token"
    ADD CONSTRAINT "Token_pkey" PRIMARY KEY (id);
 D   ALTER TABLE ONLY "zt-ehealth"."Token" DROP CONSTRAINT "Token_pkey";
    
   zt-ehealth            postgres    false    234            �           2606    16661    Usuario Usuario_cpf_key 
   CONSTRAINT     [   ALTER TABLE ONLY "zt-ehealth"."Usuario"
    ADD CONSTRAINT "Usuario_cpf_key" UNIQUE (cpf);
 K   ALTER TABLE ONLY "zt-ehealth"."Usuario" DROP CONSTRAINT "Usuario_cpf_key";
    
   zt-ehealth            postgres    false    216            �           2606    16411    Usuario Usuario_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY "zt-ehealth"."Usuario"
    ADD CONSTRAINT "Usuario_pkey" PRIMARY KEY (id);
 H   ALTER TABLE ONLY "zt-ehealth"."Usuario" DROP CONSTRAINT "Usuario_pkey";
    
   zt-ehealth            postgres    false    216            �           2606    16685 #   Acesso Acesso_idDispositivoTMP_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idDispositivoTMP_fkey" FOREIGN KEY ("idDispositivoTMP") REFERENCES "zt-ehealth"."DispositivoTMP"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 W   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idDispositivoTMP_fkey";
    
   zt-ehealth          postgres    false    3285    236    242            �           2606    16611     Acesso Acesso_idDispositivo_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idDispositivo_fkey" FOREIGN KEY ("idDispositivo") REFERENCES "zt-ehealth"."Dispositivo"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 T   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idDispositivo_fkey";
    
   zt-ehealth          postgres    false    230    3271    236            �           2606    16594    Acesso Acesso_idPermissao_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idPermissao_fkey" FOREIGN KEY ("idPermissao") REFERENCES "zt-ehealth"."Permissao"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 R   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idPermissao_fkey";
    
   zt-ehealth          postgres    false    228    236    3269            �           2606    16604 ,   Acesso Acesso_idSensibilidadeSubRecurso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idSensibilidadeSubRecurso_fkey" FOREIGN KEY ("idSensibilidadeSubRecurso") REFERENCES "zt-ehealth"."SensibilidadeSubRecurso"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 `   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idSensibilidadeSubRecurso_fkey";
    
   zt-ehealth          postgres    false    226    3267    236            �           2606    16599    Acesso Acesso_idSubRecurso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idSubRecurso_fkey" FOREIGN KEY ("idSubRecurso") REFERENCES "zt-ehealth"."SubRecurso"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 S   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idSubRecurso_fkey";
    
   zt-ehealth          postgres    false    3265    236    224            �           2606    16589    Acesso Acesso_idToken_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idToken_fkey" FOREIGN KEY ("idToken") REFERENCES "zt-ehealth"."Token"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 N   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idToken_fkey";
    
   zt-ehealth          postgres    false    3277    234    236            �           2606    16584    Acesso Acesso_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Acesso"
    ADD CONSTRAINT "Acesso_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 P   ALTER TABLE ONLY "zt-ehealth"."Acesso" DROP CONSTRAINT "Acesso_idUsuario_fkey";
    
   zt-ehealth          postgres    false    236    3257    216            �           2606    16474    Cliente Paciente_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Cliente"
    ADD CONSTRAINT "Paciente_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 S   ALTER TABLE ONLY "zt-ehealth"."Cliente" DROP CONSTRAINT "Paciente_idUsuario_fkey";
    
   zt-ehealth          postgres    false    222    3257    216            �           2606    24989 &   Permissao Permissao_idDispositivo_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Permissao"
    ADD CONSTRAINT "Permissao_idDispositivo_fkey" FOREIGN KEY ("idDispositivo") REFERENCES "zt-ehealth"."Dispositivo"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 Z   ALTER TABLE ONLY "zt-ehealth"."Permissao" DROP CONSTRAINT "Permissao_idDispositivo_fkey";
    
   zt-ehealth          postgres    false    228    230    3271            �           2606    16531 %   Permissao Permissao_idSubRecurso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Permissao"
    ADD CONSTRAINT "Permissao_idSubRecurso_fkey" FOREIGN KEY ("idSubRecurso") REFERENCES "zt-ehealth"."SubRecurso"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 Y   ALTER TABLE ONLY "zt-ehealth"."Permissao" DROP CONSTRAINT "Permissao_idSubRecurso_fkey";
    
   zt-ehealth          postgres    false    224    3265    228            �           2606    16524 "   Permissao Permissao_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Permissao"
    ADD CONSTRAINT "Permissao_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 V   ALTER TABLE ONLY "zt-ehealth"."Permissao" DROP CONSTRAINT "Permissao_idUsuario_fkey";
    
   zt-ehealth          postgres    false    3257    216    228            �           2606    16419 (   Profissional Profissional_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Profissional"
    ADD CONSTRAINT "Profissional_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 \   ALTER TABLE ONLY "zt-ehealth"."Profissional" DROP CONSTRAINT "Profissional_idUsuario_fkey";
    
   zt-ehealth          postgres    false    3257    216    218            �           2606    24994 $   RegLogin RegLogin_idDispositivo_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."RegLogin"
    ADD CONSTRAINT "RegLogin_idDispositivo_fkey" FOREIGN KEY ("idDispositivo") REFERENCES "zt-ehealth"."Dispositivo"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 X   ALTER TABLE ONLY "zt-ehealth"."RegLogin" DROP CONSTRAINT "RegLogin_idDispositivo_fkey";
    
   zt-ehealth          postgres    false    3271    232    230            �           2606    16630    RegLogin RegLogin_idSenha_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."RegLogin"
    ADD CONSTRAINT "RegLogin_idSenha_fkey" FOREIGN KEY ("idSenha") REFERENCES "zt-ehealth"."Senha"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 R   ALTER TABLE ONLY "zt-ehealth"."RegLogin" DROP CONSTRAINT "RegLogin_idSenha_fkey";
    
   zt-ehealth          postgres    false    232    3281    238            �           2606    16551     RegLogin RegLogin_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."RegLogin"
    ADD CONSTRAINT "RegLogin_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 T   ALTER TABLE ONLY "zt-ehealth"."RegLogin" DROP CONSTRAINT "RegLogin_idUsuario_fkey";
    
   zt-ehealth          postgres    false    3257    216    232            �           2606    16625    Senha Senha_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Senha"
    ADD CONSTRAINT "Senha_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 N   ALTER TABLE ONLY "zt-ehealth"."Senha" DROP CONSTRAINT "Senha_idUsuario_fkey";
    
   zt-ehealth          postgres    false    3257    216    238            �           2606    16510 A   SensibilidadeSubRecurso SensibilidadeSubRecurso_idSubRecurso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."SensibilidadeSubRecurso"
    ADD CONSTRAINT "SensibilidadeSubRecurso_idSubRecurso_fkey" FOREIGN KEY ("idSubRecurso") REFERENCES "zt-ehealth"."SubRecurso"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 u   ALTER TABLE ONLY "zt-ehealth"."SensibilidadeSubRecurso" DROP CONSTRAINT "SensibilidadeSubRecurso_idSubRecurso_fkey";
    
   zt-ehealth          postgres    false    226    224    3265            �           2606    16496 $   SubRecurso SubRecurso_idRecurso_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."SubRecurso"
    ADD CONSTRAINT "SubRecurso_idRecurso_fkey" FOREIGN KEY ("idRecurso") REFERENCES "zt-ehealth"."Recurso"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 X   ALTER TABLE ONLY "zt-ehealth"."SubRecurso" DROP CONSTRAINT "SubRecurso_idRecurso_fkey";
    
   zt-ehealth          postgres    false    220    3261    224            �           2606    24999    Token Token_idDispositivo_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Token"
    ADD CONSTRAINT "Token_idDispositivo_fkey" FOREIGN KEY ("idDispositivo") REFERENCES "zt-ehealth"."Dispositivo"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 R   ALTER TABLE ONLY "zt-ehealth"."Token" DROP CONSTRAINT "Token_idDispositivo_fkey";
    
   zt-ehealth          postgres    false    234    230    3271            �           2606    16570    Token Token_idRegLogin_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Token"
    ADD CONSTRAINT "Token_idRegLogin_fkey" FOREIGN KEY ("idRegLogin") REFERENCES "zt-ehealth"."RegLogin"(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 O   ALTER TABLE ONLY "zt-ehealth"."Token" DROP CONSTRAINT "Token_idRegLogin_fkey";
    
   zt-ehealth          postgres    false    234    232    3273            �           2606    16563    Token Token_idUsuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY "zt-ehealth"."Token"
    ADD CONSTRAINT "Token_idUsuario_fkey" FOREIGN KEY ("idUsuario") REFERENCES "zt-ehealth"."Usuario"(id) ON UPDATE CASCADE ON DELETE RESTRICT;
 N   ALTER TABLE ONLY "zt-ehealth"."Token" DROP CONSTRAINT "Token_idUsuario_fkey";
    
   zt-ehealth          postgres    false    234    3257    216            �      x������ � �      �      x������ � �      �      x�3�4����� �#      �      x������ � �      �      x������ � �      �   g  x���˪]7��;O��º�֚e�Y�'�$��p�ȥ��+�{TK:��Q�CK�/��l���}~����6��M�#���f�/AR�����������{7��w�k*�Γ�E��������#y������חO/���-;�/����h7��d��~t`8ɱ�$ْ��,�-i�q�d+���%�o�'�E&ɖ$.�H��i�M�-Q��dɎ��5 U�I�"�dK�/�H��ǎ�$[�.��%��������L��Hl�,�-iW�H�X��" `=IW��IᫍщN��Z���<ך�7>�uEi�,�M.����d��6'T��:�j�ly����8Ɖ�F�W(��E.qxFN�\�.)�&��ږ�/O�5ٜ�~�X���ٴ䢂�keܠ[^-@]Q�6���]6���#W���7;�h≺�0����&#�:7��Du��.*��3r���uMah���qm���x��PR��'�k4�z�/Jj�<.h����F�2�����&뚲Q����o��+a*<�T#�mN]��|���Х:h�[L	NF��$�-2�4�q}k��L�З�eZ�$-2I�$y�E�%-;n�l�vC�Ɓ�� ��X��\+p.�H��uGM2-��r���z5����"�LKY�ZҴ�&����)�uN�M�I�+Z�E&ɖd_d�lI��B�j$�ծ���z
���x\2�����8גm�y�5;n|�5�
턓�ej�<��p5�u�b�v�X��j�����*v�����hR��-�\��9�rɺ�b���l:f�5;TG�:[�	MU�P~�h���W�銊�F��ސQϹ8]Q�Cut�uB"�S�%;ԍZ����|0o4�E��F]�xFNtQ���ԡ�_^�f6��A��2IQs]�N5�e�2I���n׏��j�h\��'שf]S�C5R`u^�m��:T�+��l0�g���Ԣ��G祭��ޡ���9E����d�/2�nI�E����&GS�j`�%����p�ښ�نf_җM�'�O��pb�ô�c����6���lb�۳��|�R6���v^ܔOK�͕��;�1e����\J��`��� �.�to��ˆ� ��ZJ�����t>M�6R:��;:�:U�)��Q��v\I��G�quD.�t��9Lks��=^�/��,��&^��I�"�6��Efm�-F�g���.B�������1R��tu:�C�"�\Kr.�ȵ��+�Ϻ�^v�v�����x�/Ԝ-��A�!l4N�Fq�y�5��4_��f�����0�w����d�TQ6��[�}�E�%>�������J��k�c�p�V=�u���'��wԎE��6��Fa�y�j���Rլ/����b�z���M.Q�h�p��g�$��f�0+fh��˹�hn4I�Du�E���9I�d���h�r'mv��V�M.Q�h�p��3r�p�ʣg�ܲ�}D0Su�?wGcg�Y�]��M�y8�օ��$;�y�g��f��\�:\���AY7���ĥ�x��
��$
�H���t1�_�����K���n�����	m4Vd���Y���y���ܽ"M���+*��w[�0��T���g[⮪�N�H�ˎ�����w����^�      |   �   x��Ͻ
�0���]*�i���A�N
..�D���d�|_�ڤ-\�g�|��м��\�ZYݫ�Q��я���g���趢t�u
��N��Ą�d��Y%�2#��7�;m��"17� �M�6ْ�Ug��o��Xx�H�!�D�8�T�:h��_��D	&3D'�"����t�      ~   �   x�u�K
�0D��)|��CNPh��tٍ��"������L�h1 =�LW�R�P�\�-��$��)��|75����m{`�Ri��87N%H��uD?e�E�ic�,�"٭�?^;X��D_�ZRw��%փ���{���x=      �      x������ � �      �   X  x�eһ�0�X[���7sN$R91\���ػ恜! 8��@g��Xf�8�$N��67s���@�?%r����  � � ���"x�|���}\���~=@8|6B��i
q��%x�4�Ħ>ʀ��ҙr�]h�@�g�^@Ow3�7K�&�y6+���-3�O�l��UlB�GB4�wA�]_-�OCR�7ˆ���;�KJod�-���{B���><-��%�v;����t	�x�|�(]��K�$������>.7.������BA����"%�/}ɿ�8���Ys���Dκ�s7J�]��s0,�"��M����To�un�|���wO��9�[?����/��|      �   5  x�]�M�!���a"��2��d��L��"�4=#���媥�ߗ)�Ϸ������rA��u| 4V*�T��uj��>���8�}ބsE�·r���87���q�Ԏ���~Q��9�8��#?eI�C~"4b�R���%-��L9t˸�C�*�rr4�#q�CׄU(דP]�mV�NY�j.�J;ZU0���r`6�����\�o(7$v�BO�O��مР^���]]ҍJ���A�ĥ��º҅M��c��B��u*5&f�BHld*Ņ��������^�'�Ě|,a֘
�z�y�}�o�����:���>_�;���P��,��r~k_�erA�E4\l��2�0 G4��ZCF�\^BgZx	�LN&�b��6��VN߁�����D̥I���%N����Dk7\��t�����~Jw�.}�6!�i�qFI˜񲹢��i���oO�p�N%��4!%4q������es�;y��h6q[ы�v�n��`\���]ְ��aXDˎ٩o�do�E���rX� �����]riRr2�EI��/0���o��6s�      �   s  x��R�n�0<�_�/hqHx��T*D+N�l�YJl�N8��;v+
�\kgvvv�Q&���nI��?ѻ��:o�!Y�hB��IN@rM���7t�F���$�h,Y�|!���|Ǫ��Uא�py��к�������Qݛ6�*FY��f��M΅�k{p�_;u��6l[XϮ�+�(
b������$EN���0A(�oX�'��կ�Y��h�2�6�55>NL@�z*ʁ��8E�����Uo���YZ���kl�50Nit�ٚ�Ѥ9^OH����cɮv������Y ���f�&N�����"/d��m��n�:���O�|K��D1��^�]�x!7��@[z:]���۝��T�      �      x������ � �      z   �   x�e�AN�0E��)���8v�e������Q�#Y6r�����%e���^l���I�8����廈>Q�S]g�FuZ���F<�J���R*���}-'G*�h�f©`��6�}<.?��HS<a������S��n������1�G�։2�8�;�o�2M��g�����F6>��v��r�[����ʯ2�q2rZ�q���/��8,����廒R�4�c     