#!/usr/bin/env python

__description__ = "Colorize impacket's output commands."
__author__ = 'msd0pe'
__version__ = '1.0'
__date__ = '2022/07/31'

tasklist_dic = {}

tasklist_dic.update({'tl_av':["Tanium.exe", "360RP.exe", "360SD.exe", "360Safe.exe", "360leakfixer.exe", "360rp.exe", "360safe.exe", "360sd.exe", "360tray.exe", "AAWTray.exe", "ACAAS.exe", "ACAEGMgr.exe", "ACAIS.exe", "AClntUsr.EXE", "ALERT.EXE", "ALERTSVC.EXE", "ALMon.exe", "ALUNotify.exe", "ALUpdate.exe", "ALsvc.exe", "AVENGINE.exe", "AVGCHSVX.EXE", "AVGCSRVX.EXE", "AVGIDSAgent.exe", "AVGIDSMonitor.exe", "AVGIDSUI.exe", "AVGIDSWatcher.exe", "AVGNSX.EXE", "AVKProxy.exe", "AVKService.exe", "AVKTray.exe", "AVKWCtl.exe", "AVP.EXE", "AVP.exe", "AVPDTAgt.exe", "AcctMgr.exe", "Ad-Aware.exe", "Ad-Aware2007.exe", "AddressExport.exe", "AdminServer.exe", "Administrator.exe", "AeXAgentUIHost.exe", "AeXNSAgent.exe", "AeXNSRcvSvc.exe", "AlertSvc.exe", "AlogServ.exe", "AluSchedulerSvc.exe", "AnVir.exe", "AppSvc32.exe", "AtrsHost.exe", "Auth8021x.exe", "AvastSvc.exe", "AvastUI.exe", "Avconsol.exe", "AvpM.exe", "Avsynmgr.exe", "Avtask.exe", "BLACKD.exe", "BWMeterConSvc.exe", "CAAntiSpyware.exe", "CALogDump.exe", "CAPPActiveProtection.exe", "CAPPActiveProtection.exe", "CB.exe", "CCAP.EXE", "CCenter.exe", "CClaw.exe", "CLPS.exe", "CLPSLA.exe", "CLPSLS.exe", "CNTAoSMgr.exe", "CPntSrv.exe", "CTDataLoad.exe", "CertificationManagerServiceNT.exe", "ClShield.exe", "ClamTray.exe", "ClamWin.exe", "Console.exe", "CylanceUI.exe", "DAO_Log.exe", "DLService.exe", "DLTray.EXE", "DLTray.exe", "DRWAGNTD.EXE", "DRWAGNUI.EXE", "DRWEB32W.EXE", "DRWEBSCD.EXE", "DRWEBUPW.EXE", "DRWINST.EXE", "DSMain.exe", "DWHWizrd.exe", "DefWatch.exe", "DolphinCharge.exe", "EHttpSrv.exe", "EMET_Agent.exe", "EMET_Service.exe", "EMLPROUI.exe", "EMLPROXY.exe", "EMLibUpdateAgentNT.exe", "ETConsole3.exe", "ETCorrel.exe", "ETLogAnalyzer.exe", "ETReporter.exe", "ETRssFeeds.exe", "EUQMonitor.exe", "EndPointSecurity.exe", "EngineServer.exe", "EntityMain.exe", "EtScheduler.exe", "EtwControlPanel.exe", "EventParser.exe", "FAMEH32.exe", "FCDBLog.exe", "FCH32.exe", "FPAVServer.exe", "FProtTray.exe", "FSCUIF.exe", "FSHDLL32.exe", "FSM32.exe", "FSMA32.exe", "FSMB32.exe", "FWCfg.exe", "FireSvc.exe", "FireTray.exe", "FirewallGUI.exe", "ForceField.exe", "FortiProxy.exe", "FortiTray.exe", "FortiWF.exe", "FrameworkService.exe", "FreeProxy.exe", "GDFirewallTray.exe", "GDFwSvc.exe", "HWAPI.exe", "ISNTSysMonitor.exe", "ISSVC.exe", "ISWMGR.exe", "ITMRTSVC.exe", "ITMRT_SupportDiagnostics.exe", "ITMRT_TRACE.exe", "IcePack.exe", "IdsInst.exe", "InoNmSrv.exe", "InoRT.exe", "InoRpc.exe", "InoTask.exe", "InoWeb.exe", "IsntSmtp.exe", "KABackReport.exe", "KANMCMain.exe", "KAVFS.EXE", "KAVStart.exe", "KLNAGENT.EXE", "KMailMon.exe", "KNUpdateMain.exe", "KPFWSvc.exe", "KSWebShield.exe", "KVMonXP.exe", "KVMonXP_2.exe", "KVSrvXP.exe", "KWSProd.exe", "KWatch.exe", "KavAdapterExe.exe", "KeyPass.exe", "KvXP.exe", "LUALL.EXE", "LWDMServer.exe", "LockApp.exe", "LockAppHost.exe", "LogGetor.exe", "MCSHIELD.EXE", "MCUI32.exe", "MSASCui.exe", "ManagementAgentNT.exe", "McAfeeDataBackup.exe", "McEPOC.exe", "McEPOCfg.exe", "McNASvc.exe", "McProxy.exe", "McScript_InUse.exe", "McWCE.exe", "McWCECfg.exe", "Mcshield.exe", "Mctray.exe", "MgntSvc.exe", "MpCmdRun.exe", "MpfAgent.exe", "MpfSrv.exe", "MsMpEng.exe", "NAIlgpip.exe", "NAVAPSVC.EXE", "NAVAPW32.EXE", "NCDaemon.exe", "NIP.exe", "NJeeves.exe", "NLClient.exe", "NMAGENT.EXE", "NOD32view.exe", "NPFMSG.exe", "NPROTECT.EXE", "NRMENCTB.exe", "NSMdtr.exe", "NTRtScan.exe", "NVCOAS.exe", "NVCSched.exe", "NavShcom.exe", "Navapsvc.exe", "NaveCtrl.exe", "NaveLog.exe", "NaveSP.exe", "Navw32.exe", "Navwnt.exe", "Nip.exe", "Njeeves.exe", "Npfmsg2.exe", "Npfsvice.exe", "NscTop.exe", "Nvcoas.exe", "Nvcsched.exe", "Nymse.exe", "OLFSNT40.EXE", "OMSLogManager.exe", "ONLINENT.exe", "ONLNSVC.exe", "OfcPfwSvc.exe", "PASystemTray.exe", "PAVFNSVR.exe", "PAVSRV51.exe", "PNmSrv.exe", "POPROXY.EXE", "POProxy.exe", "PPClean.exe", "PPCtlPriv.exe", "PQIBrowser.exe", "PSHost.exe", "PSIMSVC.EXE", "PXEMTFTP.exe", "PadFSvr.exe", "Pagent.exe", "Pagentwd.exe", "PavBckPT.exe", "PavFnSvr.exe", "PavPrSrv.exe", "PavProt.exe", "PavReport.exe", "Pavkre.exe", "PcCtlCom.exe", "PcScnSrv.exe", "PccNTMon.exe", "PccNTUpd.exe", "PpPpWallRun.exe", "PrintDevice.exe", "ProUtil.exe", "PsCtrlS.exe", "PsImSvc.exe", "PwdFiltHelp.exe", "Qoeloader.exe", "RAVMOND.exe", "RAVXP.exe", "RNReport.exe", "RPCServ.exe", "RSSensor.exe", "RTVscan.exe", "RapApp.exe", "Rav.exe", "RavAlert.exe", "RavMon.exe", "RavMonD.exe", "RavService.exe", "RavStub.exe", "RavTask.exe", "RavTray.exe", "RavUpdate.exe", "RavXP.exe", "RealMon.exe", "Realmon.exe", "RedirSvc.exe", "RegMech.exe", "ReporterSvc.exe", "RouterNT.exe", "Rtvscan.exe", "SAFeService.exe", "SAService.exe", "SAVAdminService.exe", "SAVFMSESp.exe", "SAVMain.exe", "SAVScan.exe", "SCANMSG.exe", "SCANWSCS.exe", "SCFManager.exe", "SCFService.exe", "SCFTray.exe", "SDTrayApp.exe", "SEVINST.EXE", "SMEX_ActiveUpdate.exe", "SMEX_Master.exe", "SMEX_RemoteConf.exe", "SMEX_SystemWatch.exe", "SMSECtrl.exe", "SMSELog.exe", "SMSESJM.exe", "SMSESp.exe", "SMSESrv.exe", "SMSETask.exe", "SMSEUI.exe", "SNAC.EXE", "SNAC.exe", "SNDMon.exe", "SNDSrvc.exe", "SPBBCSvc.exe", "SPIDERML.EXE", "SPIDERNT.EXE", "SSM.exe", "SSScheduler.exe", "SVCharge.exe", "SVDealer.exe", "SVFrame.exe", "SVTray.exe", "SWNETSUP.EXE", "SavRoam.exe", "SavService.exe", "SavUI.exe", "ScanMailOutLook.exe", "SeAnalyzerTool.exe", "SemSvc.exe", "SescLU.exe", "SetupGUIMngr.exe", "SiteAdv.exe", "Smc.exe", "SmcGui.exe", "SnHwSrv.exe", "SnICheckAdm.exe", "SnIcon.exe", "SnSrv.exe", "SnicheckSrv.exe", "SpIDerAgent.exe", "SpntSvc.exe", "SpyEmergency.exe", "SpyEmergencySrv.exe", "StOPP.exe", "StWatchDog.exe", "SymCorpUI.exe", "SymSPort.exe", "TBMon.exe", "TFGui.exe", "TFService.exe", "TFTray.exe", "TFun.exe", "TIASPN~1.EXE", "TSAnSrf.exe", "TSAtiSy.exe", "TScutyNT.exe", "TSmpNT.exe", "TmListen.exe", "TmPfw.exe", "Tmntsrv.exe", "Traflnsp.exe", "TrapTrackerMgr.exe", "UPSCHD.exe", "UcService.exe", "UdaterUI.exe", "UmxAgent.exe", "UmxCfg.exe", "UmxFwHlp.exe", "UmxPol.exe", "Up2date.exe", "UpdaterUI.exe", "UrlLstCk.exe", "UserActivity.exe", "UserAnalysis.exe", "UsrPrmpt.exe", "V3Medic.exe", "V3Svc.exe", "VPC32.exe", "VPDN_LU.exe", "VPTray.exe", "VSStat.exe", "VsStat.exe", "VsTskMgr.exe", "WEBPROXY.EXE", "WFXCTL32.EXE", "WFXMOD32.EXE", "WFXSNT40.EXE", "WebProxy.exe", "WebScanX.exe", "WinRoute.exe", "WrSpySetup.exe", "ZLH.exe", "Zanda.exe", "ZhuDongFangYu.exe", "Zlh.exe", "_avp32.exe", "_avpcc.exe", "_avpm.exe", "aAvgApi.exe", "aawservice.exe", "acaif.exe", "acctmgr.exe", "ackwin32.exe", "aclient.exe", "adaware.exe", "advxdwin.exe", "aexnsagent.exe", "aexsvc.exe", "aexswdusr.exe", "aflogvw.exe", "afwServ.exe", "agentsvr.exe", "agentw.exe", "ahnrpt.exe", "ahnsd.exe", "ahnsdsv.exe", "alertsvc.exe", "alevir.exe", "alogserv.exe", "alsvc.exe", "alunotify.exe", "aluschedulersvc.exe", "amon9x.exe", "amswmagt.exe", "anti-trojan.exe", "antiarp.exe", "antivirus.exe", "ants.exe", "aphost.exe", "apimonitor.exe", "aplica32.exe", "aps.exe", "apvxdwin.exe", "arr.exe", "ashAvast.exe", "ashBug.exe", "ashChest.exe", "ashCmd.exe", "ashDisp.exe", "ashEnhcd.exe", "ashLogV.exe", "ashMaiSv.exe", "ashPopWz.exe", "ashQuick.exe", "ashServ.exe", "ashSimp2.exe", "ashSimpl.exe", "ashSkPcc.exe", "ashSkPck.exe", "ashUpd.exe", "ashWebSv.exe", "ashdisp.exe", "ashmaisv.exe", "ashserv.exe", "ashwebsv.exe", "asupport.exe", "aswDisp.exe", "aswRegSvr.exe", "aswServ.exe", "aswUpdSv.exe", "aswUpdsv.exe", "aswWebSv.exe", "aswupdsv.exe", "atcon.exe", "atguard.exe", "atro55en.exe", "atupdater.exe", "atwatch.exe", "atwsctsk.exe", "au.exe", "aupdate.exe", "aupdrun.exe", "aus.exe", "auto-protect.nav80try.exe", "autodown.exe", "autotrace.exe", "autoup.exe", "autoupdate.exe", "avEngine.exe", "avadmin.exe", "avcenter.exe", "avconfig.exe", "avconsol.exe", "ave32.exe", "avengine.exe", "avesvc.exe", "avfwsvc.exe", "avgam.exe", "avgamsvr.exe", "avgas.exe", "avgcc.exe", "avgcc32.exe", "avgcsrvx.exe", "avgctrl.exe", "avgdiag.exe", "avgemc.exe", "avgfws8.exe", "avgfws9.exe", "avgfwsrv.exe", "avginet.exe", "avgmsvr.exe", "avgnsx.exe", "avgnt.exe", "avgregcl.exe", "avgrssvc.exe", "avgrsx.exe", "avgscanx.exe", "avgserv.exe", "avgserv9.exe", "avgsystx.exe", "avgtray.exe", "avguard.exe", "avgui.exe", "avgupd.exe", "avgupdln.exe", "avgupsvc.exe", "avgvv.exe", "avgw.exe", "avgwb.exe", "avgwdsvc.exe", "avgwizfw.exe", "avkpop.exe", "avkserv.exe", "avkservice.exe", "avkwctl9.exe", "avltmain.exe", "avmailc.exe", "avmcdlg.exe", "avnotify.exe", "avnt.exe", "avp.exe", "avp32.exe", "avpcc.exe", "avpdos32.exe", "avpexec.exe", "avpm.exe", "avpncc.exe", "avps.exe", "avptc32.exe", "avpupd.exe", "avscan.exe", "avsched32.exe", "avserver.exe", "avshadow.exe", "avsynmgr.exe", "avwebgrd.exe", "avwin.exe", "avwin95.exe", "avwinnt.exe", "avwupd.exe", "avwupd32.exe", "avwupsrv.exe", "avxmonitor9x.exe", "avxmonitornt.exe", "avxquar.exe", "backweb.exe", "bargains.exe", "basfipm.exe", "bd_professional.exe", "bdagent.exe", "bdc.exe", "bdlite.exe", "bdmcon.exe", "bdss.exe", "bdsubmit.exe", "beagle.exe", "belt.exe", "bidef.exe", "bidserver.exe", "bipcp.exe", "bipcpevalsetup.exe", "bisp.exe", "blackd.exe", "blackice.exe", "blink.exe", "blss.exe", "bmrt.exe", "bootconf.exe", "bootwarn.exe", "borg2.exe", "bpc.exe", "bpk.exe", "brasil.exe", "bs120.exe", "bundle.exe", "bvt.exe", "bwgo0000.exe", "ca.exe", "caav.exe", "caavcmdscan.exe", "caavguiscan.exe", "caf.exe", "cafw.exe", "caissdt.exe", "capfaem.exe", "capfasem.exe", "capfsem.exe", "capmuamagt.exe", "casc.exe", "casecuritycenter.exe", "caunst.exe", "cavrep.exe", "cavrid.exe", "cavscan.exe", "cavtray.exe", "ccApp.exe", "ccEvtMgr.exe", "ccLgView.exe", "ccProxy.exe", "ccSetMgr.exe", "ccSetmgr.exe", "ccSvcHst.exe", "ccap.exe", "ccapp.exe", "ccevtmgr.exe", "cclaw.exe", "ccnfagent.exe", "ccprovsp.exe", "ccproxy.exe", "ccpxysvc.exe", "ccschedulersvc.exe", "ccsetmgr.exe", "ccsmagtd.exe", "ccsvchst.exe", "ccsystemreport.exe", "cctray.exe", "ccupdate.exe", "cdp.exe", "cfd.exe", "cfftplugin.exe", "cfgwiz.exe", "cfiadmin.exe", "cfiaudit.exe", "cfinet.exe", "cfinet32.exe", "cfnotsrvd.exe", "cfp.exe", "cfpconfg.exe", "cfpconfig.exe", "cfplogvw.exe", "cfpsbmit.exe", "cfpupdat.exe", "cfsmsmd.exe", "checkup.exe", "cka.exe", "clamscan.exe", "claw95.exe", "claw95cf.exe", "clean.exe", "cleaner.exe", "cleaner3.exe", "cleanpc.exe", "cleanup.exe", "click.exe", "cmdagent.exe", "cmdinstall.exe", "cmesys.exe", "cmgrdian.exe", "cmon016.exe", "comHost.exe", "connectionmonitor.exe", "control_panel.exe", "cpd.exe", "cpdclnt.exe", "cpf.exe", "cpf9x206.exe", "cpfnt206.exe", "crashrep.exe", "csacontrol.exe", "csinject.exe", "csinsm32.exe", "csinsmnt.exe", "csrss_tc.exe", "ctrl.exe", "cv.exe", "cwnb181.exe", "cwntdwmo.exe", "cz.exe", "datemanager.exe", "dbserv.exe", "dbsrv9.exe", "dcomx.exe", "defalert.exe", "defscangui.exe", "defwatch.exe", "deloeminfs.exe", "deputy.exe", "diskmon.exe", "divx.exe", "djsnetcn.exe", "dllcache.exe", "dllreg.exe", "doors.exe", "doscan.exe", "dpf.exe", "dpfsetup.exe", "dpps2.exe", "drwagntd.exe", "drwatson.exe", "drweb.exe", "drweb32.exe", "drweb32w.exe", "drweb386.exe", "drwebcgp.exe", "drwebcom.exe", "drwebdc.exe", "drwebmng.exe", "drwebscd.exe", "drwebupw.exe", "drwebwcl.exe", "drwebwin.exe", "drwupgrade.exe", "dsmain.exe", "dssagent.exe", "dvp95.exe", "dvp95_0.exe", "dwengine.exe", "dwhwizrd.exe", "dwwin.exe", "ecengine.exe", "edisk.exe", "efpeadm.exe", "egui.exe", "ekrn.exe", "elogsvc.exe", "emet_agent.exe", "emet_service.exe", "emsw.exe", "engineserver.exe", "ent.exe", "era.exe", "esafe.exe", "escanhnt.exe", "escanv95.exe", "esecagntservice.exe", "esecservice.exe", "esmagent.exe", "espwatch.exe", "etagent.exe", "ethereal.exe", "etrustcipe.exe", "evpn.exe", "evtProcessEcFile.exe", "evtarmgr.exe", "evtmgr.exe", "exantivirus-cnet.exe", "exe.avxw.exe", "execstat.exe", "expert.exe", "explore.exe", "f-agnt95.exe", "f-prot.exe", "f-prot95.exe", "f-stopw.exe", "fameh32.exe", "fast.exe", "fch32.exe", "fih32.exe", "findviru.exe", "firesvc.exe", "firetray.exe", "firewall.exe", "fmon.exe", "fnrb32.exe", "fortifw.exe", "fp-win.exe", "fp-win_trial.exe", "fprot.exe", "frameworkservice.exe", "frminst.exe", "frw.exe", "fsaa.exe", "fsaua.exe", "fsav.exe", "fsav32.exe", "fsav530stbyb.exe", "fsav530wtbyb.exe", "fsav95.exe", "fsavgui.exe", "fscuif.exe", "fsdfwd.exe", "fsgk32.exe", "fsgk32st.exe", "fsguidll.exe", "fsguiexe.exe", "fshdll32.exe", "fsm32.exe", "fsma32.exe", "fsmb32.exe", "fsorsp.exe", "fspc.exe", "fspex.exe", "fsqh.exe", "fssm32.exe", "fwinst.exe", "gator.exe", "gbmenu.exe", "gbpoll.exe", "gcascleaner.exe", "gcasdtserv.exe", "gcasinstallhelper.exe", "gcasnotice.exe", "gcasserv.exe", "gcasservalert.exe", "gcasswupdater.exe", "generics.exe", "gfireporterservice.exe", "ghost_2.exe", "ghosttray.exe", "giantantispywaremain.exe", "giantantispywareupdater.exe", "gmt.exe", "guard.exe", "guarddog.exe", "guardgui.exe", "hacktracersetup.exe", "hbinst.exe", "hbsrv.exe", "hipsvc.exe", "hotactio.exe", "hotpatch.exe", "htlog.exe", "htpatch.exe", "hwpe.exe", "hxdl.exe", "hxiul.exe", "iamapp.exe", "iamserv.exe", "iamstats.exe", "ibmasn.exe", "ibmavsp.exe", "icepack.exe", "icload95.exe", "icloadnt.exe", "icmon.exe", "icsupp95.exe", "icsuppnt.exe", "idle.exe", "iedll.exe", "iedriver.exe", "iface.exe", "ifw2000.exe", "igateway.exe", "inetlnfo.exe", "infus.exe", "infwin.exe", "inicio.exe", "init.exe", "inonmsrv.exe", "inorpc.exe", "inort.exe", "inotask.exe", "intdel.exe", "intren.exe", "iomon98.exe", "isPwdSvc.exe", "isUAC.exe", "isafe.exe", "isafinst.exe", "issvc.exe", "istsvc.exe", "jammer.exe", "jdbgmrg.exe", "jedi.exe", "kaccore.exe", "kansgui.exe", "kansvr.exe", "kastray.exe", "kav.exe", "kav32.exe", "kavfs.exe", "kavfsgt.exe", "kavfsrcn.exe", "kavfsscs.exe", "kavfswp.exe", "kavisarv.exe", "kavlite40eng.exe", "kavlotsingleton.exe", "kavmm.exe", "kavpers40eng.exe", "kavpf.exe", "kavshell.exe", "kavss.exe", "kavstart.exe", "kavsvc.exe", "kavtray.exe", "kazza.exe", "keenvalue.exe", "kerio-pf-213-en-win.exe", "kerio-wrl-421-en-win.exe", "kerio-wrp-421-en-win.exe", "kernel32.exe", "killprocesssetup161.exe", "kis.exe", "kislive.exe", "kissvc.exe", "klnacserver.exe", "klnagent.exe", "klserver.exe", "klswd.exe", "klwtblfs.exe", "kmailmon.exe", "knownsvr.exe", "kpf4gui.exe", "kpf4ss.exe", "kpfw32.exe", "kpfwsvc.exe", "krbcc32s.exe", "kvdetech.exe", "kvolself.exe", "kvsrvxp.exe", "kvsrvxp_1.exe", "kwatch.exe", "kwsprod.exe", "kxeserv.exe", "launcher.exe", "ldnetmon.exe", "ldpro.exe", "ldpromenu.exe", "ldscan.exe", "leventmgr.exe", "livesrv.exe", "lmon.exe", "lnetinfo.exe", "loader.exe", "localnet.exe", "lockdown.exe", "lockdown2000.exe", "log_qtine.exe", "lookout.exe", "lordpe.exe", "lsetup.exe", "luall.exe", "luau.exe", "lucallbackproxy.exe", "lucoms.exe", "lucomserver.exe", "lucoms~1.exe", "luinit.exe", "luspt.exe", "makereport.exe", "mantispm.exe", "mapisvc32.exe", "masalert.exe", "massrv.exe", "mcafeefire.exe", "mcagent.exe", "mcappins.exe", "mcconsol.exe", "mcdash.exe", "mcdetect.exe", "mcepoc.exe", "mcepocfg.exe", "mcinfo.exe", "mcmnhdlr.exe", "mcmscsvc.exe", "mcods.exe", "mcpalmcfg.exe", "mcpromgr.exe", "mcregwiz.exe", "mcscript.exe", "mcscript_inuse.exe", "mcshell.exe", "mcshield.exe", "mcshld9x.exe", "mcsysmon.exe", "mctool.exe", "mctray.exe", "mctskshd.exe", "mcuimgr.exe", "mcupdate.exe", "mcupdmgr.exe", "mcvsftsn.exe", "mcvsrte.exe", "mcvsshld.exe", "mcwce.exe", "mcwcecfg.exe", "md.exe", "mfeann.exe", "mfevtps.exe", "mfin32.exe", "mfw2en.exe", "mfweng3.02d30.exe", "mgavrtcl.exe", "mgavrte.exe", "mghtml.exe", "mgui.exe", "minilog.exe", "mmod.exe", "monitor.exe", "monsvcnt.exe", "monsysnt.exe", "moolive.exe", "mostat.exe", "mpcmdrun.exe", "mpf.exe", "mpfagent.exe", "mpfconsole.exe", "mpfservice.exe", "mpftray.exe", "mps.exe", "mpsevh.exe", "mpsvc.exe", "mrf.exe", "mrflux.exe", "msapp.exe", "msascui.exe", "msbb.exe", "msblast.exe", "mscache.exe", "msccn32.exe", "mscifapp.exe", "mscman.exe", "msconfig.exe", "msdm.exe", "msdos.exe", "msiexec16.exe", "mskagent.exe", "mskdetct.exe", "msksrver.exe", "msksrvr.exe", "mslaugh.exe", "msmgt.exe", "msmpeng.exe", "msmsgri32.exe", "msscli.exe", "msseces.exe", "mssmmc32.exe", "msssrv.exe", "mssys.exe", "msvxd.exe", "mu0311ad.exe", "mwatch.exe", "myagttry.exe", "n32scanw.exe", "nSMDemf.exe", "nSMDmon.exe", "nSMDreal.exe", "nSMDsch.exe", "naPrdMgr.exe", "nav.exe", "navap.navapsvc.exe", "navapsvc.exe", "navapw32.exe", "navdx.exe", "navlu32.exe", "navnt.exe", "navstub.exe", "navw32.exe", "navwnt.exe", "nc2000.exe", "ncinst4.exe", "MsSense.exe", "SenseCncProxy.exe", "SenseSampleUploader.exe", "MSASCuiL.exe", "CylanceSvc.exe", "ndd32.exe", "ndetect.exe", "neomonitor.exe", "neotrace.exe", "neowatchlog.exe", "netalertclient.exe", "netarmor.exe", "netcfg.exe", "netd32.exe", "netinfo.exe", "netmon.exe", "netscanpro.exe", "netspyhunter-1.2.exe", "netstat.exe", "netutils.exe", "networx.exe", "ngctw32.exe", "ngserver.exe", "nip.exe", "nipsvc.exe", "nisoptui.exe", "nisserv.exe", "nisum.exe", "njeeves.exe", "nlsvc.exe", "nmain.exe", "nod32.exe", "nod32krn.exe", "nod32kui.exe", "normist.exe", "norton_internet_secu_3.0_407.exe", "notstart.exe", "npf40_tw_98_nt_me_2k.exe", "npfmessenger.exe", "npfmntor.exe", "npfmsg.exe", "nprotect.exe", "npscheck.exe", "npssvc.exe", "nrmenctb.exe", "nsched32.exe", "nscsrvce.exe", "nsctop.exe", "nsmdtr.exe", "nssys32.exe", "nstask32.exe", "nsupdate.exe", "nt.exe", "ntcaagent.exe", "ntcadaemon.exe", "ntcaservice.exe", "ntrtscan.exe", "ntvdm.exe", "ntxconfig.exe", "nui.exe", "nupgrade.exe", "nvarch16.exe", "nvc95.exe", "nvcoas.exe", "nvcsched.exe", "nvsvc32.exe", "nwinst4.exe", "nwservice.exe", "nwtool16.exe", "nymse.exe", "oasclnt.exe", "oespamtest.exe", "ofcdog.exe", "ofcpfwsvc.exe", "okclient.exe", "olfsnt40.exe", "ollydbg.exe", "onsrvr.exe", "op_viewer.exe", "opscan.exe", "optimize.exe", "ostronet.exe", "otfix.exe", "outpost.exe", "outpostinstall.exe", "outpostproinstall.exe", "paamsrv.exe", "padmin.exe", "pagent.exe", "pagentwd.exe", "panixk.exe", "patch.exe", "pavbckpt.exe", "pavcl.exe", "pavfires.exe", "pavfnsvr.exe", "pavjobs.exe", "pavkre.exe", "pavmail.exe", "pavprot.exe", "pavproxy.exe", "pavprsrv.exe", "pavsched.exe", "pavsrv50.exe", "pavsrv51.exe", "pavsrv52.exe", "pavupg.exe", "pavw.exe", "pccNT.exe", "pccclient.exe", "pccguide.exe", "pcclient.exe", "pccnt.exe", "pccntmon.exe", "pccntupd.exe", "pccpfw.exe", "pcctlcom.exe", "pccwin98.exe", "pcfwallicon.exe", "pcip10117_0.exe", "pcscan.exe", "pctsAuxs.exe", "pctsGui.exe", "pctsSvc.exe", "pctsTray.exe", "pdsetup.exe", "pep.exe", "periscope.exe", "persfw.exe", "perswf.exe", "pf2.exe", "pfwadmin.exe", "pgmonitr.exe", "pingscan.exe", "platin.exe", "pmon.exe", "pnmsrv.exe", "pntiomon.exe", "pop3pack.exe", "pop3trap.exe", "poproxy.exe", "popscan.exe", "portdetective.exe", "portmonitor.exe", "powerscan.exe", "ppinupdt.exe", "ppmcativedetection.exe", "pptbc.exe", "ppvstop.exe", "pqibrowser.exe", "pqv2isvc.exe", "prevsrv.exe", "prizesurfer.exe", "prmt.exe", "prmvr.exe", "programauditor.exe", "proport.exe", "protectx.exe", "psctris.exe", "psh_svc.exe", "psimreal.exe", "psimsvc.exe", "pskmssvc.exe", "pspf.exe", "purge.exe", "pview.exe", "pviewer.exe", "pxemtftp.exe", "pxeservice.exe", "qclean.exe", "qconsole.exe", "qdcsfs.exe", "qoeloader.exe", "qserver.exe", "rapapp.exe", "rapuisvc.exe", "ras.exe", "rasupd.exe", "rav7.exe", "rav7win.exe", "rav8win32eng.exe", "ravmon.exe", "ravmond.exe", "ravstub.exe", "ravxp.exe", "ray.exe", "rb32.exe", "rcsvcmon.exe", "rcsync.exe", "realmon.exe", "reged.exe", "remupd.exe", "reportsvc.exe", "rescue.exe", "rescue32.exe", "rfwmain.exe", "rfwproxy.exe", "rfwsrv.exe", "rfwstub.exe", "rnav.exe", "rrguard.exe", "rshell.exe", "rsnetsvr.exe", "rstray.exe", "rtvscan.exe", "rtvscn95.exe", "rulaunch.exe", "saHookMain.exe", "safeboxtray.exe", "safeweb.exe", "sahagent.exescan32.exe", "sav32cli.exe", "save.exe", "savenow.exe", "savroam.exe", "savscan.exe", "savservice.exe", "sbserv.exe", "scam32.exe", "scan32.exe", "scan95.exe", "scanexplicit.exe", "scanfrm.exe", "scanmailoutlook.exe", "scanpm.exe", "schdsrvc.exe", "schupd.exe", "scrscan.exe", "seestat.exe", "serv95.exe", "setloadorder.exe", "setup_flowprotector_us.exe", "setupguimngr.exe", "setupvameeval.exe", "sfc.exe", "sgssfw32.exe", "sh.exe", "shellspyinstall.exe", "shn.exe", "showbehind.exe", "shstat.exe", "siteadv.exe", "smOutlookPack.exe", "smc.exe", "smoutlookpack.exe", "sms.exe", "smsesp.exe", "smss32.exe", "sndmon.exe", "sndsrvc.exe", "soap.exe", "sofi.exe", "softManager.exe", "spbbcsvc.exe", "spf.exe", "sphinx.exe", "spideragent.exe", "spiderml.exe", "spidernt.exe", "spiderui.exe", "spntsvc.exe", "spoler.exe", "spoolcv.exe", "spoolsv32.exe", "spyxx.exe", "srexe.exe", "srng.exe", "srvload.exe", "srvmon.exe", "ss3edit.exe", "sschk.exe", "ssg_4104.exe", "ssgrate.exe", "st2.exe", "stcloader.exe", "stinger.exe", "stopp.exe", "stwatchdog.exe", "supftrl.exe", "support.exe", "supporter5.exe", "svcGenericHost", "svcharge.exe", "svchostc.exe", "svchosts.exe", "svcntaux.exe", "svdealer.exe", "svframe.exe", "svtray.exe", "swdsvc.exe", "sweep95.exe", "sweepnet.sweepsrv.sys.swnetsup.exe", "sweepsrv.exe", "swnetsup.exe", "swnxt.exe", "swserver.exe", "symlcsvc.exe", "symproxysvc.exe", "symsport.exe", "symtray.exe", "symwsc.exe", "sysdoc32.exe", "sysedit.exe", "sysupd.exe", "taskmo.exe", "taumon.exe", "tbmon.exe", "tbscan.exe", "tc.exe", "tca.exe", "tclproc.exe", "tcm.exe", "tdimon.exe", "tds-3.exe", "tds2-98.exe", "tds2-nt.exe", "teekids.exe", "tfak.exe", "tfak5.exe", "tgbob.exe", "titanin.exe", "titaninxp.exe", "tmas.exe", "tmlisten.exe", "tmntsrv.exe", "tmpfw.exe", "tmproxy.exe", "tnbutil.exe", "tpsrv.exe", "tracesweeper.exe", "trickler.exe", "trjscan.exe", "trjsetup.exe", "trojantrap3.exe", "trupd.exe", "tsadbot.exe", "tvmd.exe", "tvtmd.exe", "udaterui.exe", "undoboot.exe", "unvet32.exe", "updat.exe", "updtnv28.exe", "upfile.exe", "upgrad.exe", "uplive.exe", "urllstck.exe", "usergate.exe", "usrprmpt.exe", "utpost.exe", "v2iconsole.exe", "v3clnsrv.exe", "v3exec.exe", "v3imscn.exe", "vbcmserv.exe", "vbcons.exe", "vbust.exe", "vbwin9x.exe", "vbwinntw.exe", "vcsetup.exe", "vet32.exe", "vet95.exe", "vetmsg.exe", "vettray.exe", "vfsetup.exe", "vir-help.exe", "virusmdpersonalfirewall.exe", "vnlan300.exe", "vnpc3000.exe", "vpatch.exe", "vpc32.exe", "vpc42.exe", "vpfw30s.exe", "vprosvc.exe", "vptray.exe", "vrv.exe", "vrvmail.exe", "vrvmon.exe", "vrvnet.exe", "vscan40.exe", "vscenu6.02d30.exe", "vsched.exe", "vsecomr.exe", "vshwin32.exe", "vsisetup.exe", "vsmain.exe", "vsmon.exe", "vsserv.exe", "vsstat.exe", "vstskmgr.exe", "vswin9xe.exe", "vswinntse.exe", "vswinperse.exe", "w32dsm89.exe", "w9x.exe", "watchdog.exe", "webdav.exe", "webproxy.exe", "webscanx.exe", "webtrap.exe", "webtrapnt.exe", "wfindv32.exe", "wfxctl32.exe", "wfxmod32.exe", "wfxsnt40.exe", "whoswatchingme.exe", "wimmun32.exe", "win-bugsfix.exe", "winactive.exe", "winmain.exe", "winnet.exe", "winppr32.exe", "winrecon.exe", "winroute.exe", "winservn.exe", "winssk32.exe", "winstart.exe", "winstart001.exe", "wintsk32.exe", "winupdate.exe", "wkufind.exe", "wnad.exe", "wnt.exe", "wradmin.exe", "wrctrl.exe", "wsbgate.exe", "wssfcmai.exe", "wupdater.exe", "wupdt.exe", "wyvernworksfirewall.exe", "xagt.exe", "xagtnotif.exe", "xcommsvr.exe", "xfilter.exe", "xpf202en.exe", "zanda.exe", "zapro.exe", "zapsetup3001.exe", "zatutor.exe", "zhudongfangyu.exe", "zlclient.exe", "zlh.exe", "zonalm2601.exe", "zonealarm.exe",  "mfecanary.exe", "mfeesp.exe", "mfefire.exe", "mfefw.exe", "mfehcs.exe", "mfemactl.exe", "mfemms.exe", "mfetp.exe", "mfewc.exe", "CSFalconService.exe", "CSFalconContainer.exe", "SophosFIMService.exe", "SophosFS.exe", "Sophos UI.exe", "SophosFileScanner.exe", "SAVAdminService.exe", "ALsvc.exe", "Clean.exe", "sdcservice.exe", "SEDService.exe", "SSPService.exe", "SophosFIMService.exe", "SophosFileScanner.exe", "SophosFS.exe", "Health.exe", "McsAgent.exe", "McsClient.exe", "SntpService.exe", "Safestore64.exe", "hmpalert.exe", "swi_service.exe", "swi_fc.exe", "swi_filter.exe"]})

tasklist_dic.update({'tl_admin':["MobaXterm.exe", "bash.exe", "git-bash.exe", "mmc.exe", "tasklist.exe", "Code.exe", "notepad++.exe", "notepad.exe", "cmd.exe", "drwatson.exe", "DRWTSN32.EXE", "drwtsn32.exe", "dumpcap.exe", "ethereal.exe", "filemon.exe", "idag.exe", "idaw.exe", "k1205.exe", "loader32.exe", "netmon.exe", "netstat.exe", "netxray.exe", "NmWebService.exe", "nukenabber.exe", "portmon.exe", "powershell.exe", "PRTG Traffic Gr.exe", "PRTG Traffic Grapher.exe", "prtgwatchdog.exe", "putty.exe", "regmon.exe", "SystemEye.exe", "taskman.exe", "TASKMGR.EXE", "tcpview.exe", "Totalcmd.exe", "TrafMonitor.exe", "windbg.exe", "winobj.exe", "wireshark.exe", "WMonAvNScan.exe", "WMonAvScan.exe", "WMonSrv.exe","regedit.exe", "regedit32.exe", "accesschk.exe", "accesschk64.exe", "AccessEnum.exe", "ADExplorer.exe", "ADInsight.exe", "adrestore.exe", "Autologon.exe", "Autoruns.exe", "Autoruns64.exe", "autorunsc.exe", "autorunsc64.exe", "Bginfo.exe", "Bginfo64.exe", "Cacheset.exe", "Clockres.exe", "Clockres64.exe", "Contig.exe", "Contig64.exe", "Coreinfo.exe", "ctrl2cap.exe", "Dbgview.exe", "Desktops.exe", "disk2vhd.exe", "diskext.exe", "diskext64.exe", "Diskmon.exe", "DiskView.exe", "du.exe", "du64.exe", "efsdump.exe", "FindLinks.exe", "FindLinks64.exe", "handle.exe", "handle64.exe", "hex2dec.exe", "hex2dec64.exe", "junction.exe", "junction64.exe", "ldmdump.exe", "Listdlls.exe", "Listdlls64.exe", "livekd.exe", "livekd64.exe", "LoadOrd.exe", "LoadOrd64.exe", "LoadOrdC.exe", "LoadOrdC64.exe", "logonsessions.exe", "logonsessions64.exe", "movefile.exe", "movefile64.exe", "notmyfault.exe", "notmyfault64.exe", "notmyfaultc.exe", "notmyfaultc64.exe", "ntfsinfo.exe", "ntfsinfo64.exe", "pagedfrg.exe", "pendmoves.exe", "pendmoves64.exe", "pipelist.exe", "pipelist64.exe", "portmon.exe", "procdump.exe", "procdump64.exe", "procexp.exe", "procexp64.exe", "Procmon.exe", "PsExec.exe", "PsExec64.exe", "psfile.exe", "psfile64.exe", "PsGetsid.exe", "PsGetsid64.exe", "PsInfo.exe", "PsInfo64.exe", "pskill.exe", "pskill64.exe", "pslist.exe", "pslist64.exe", "PsLoggedon.exe", "PsLoggedon64.exe", "psloglist.exe", "pspasswd.exe", "pspasswd64.exe", "psping.exe", "psping64.exe", "PsService.exe", "PsService64.exe", "psshutdown.exe", "pssuspend.exe", "pssuspend64.exe", "RAMMap.exe", "RegDelNull.exe", "RegDelNull64.exe", "regjump.exe", "ru.exe", "ru64.exe", "sdelete.exe", "sdelete64.exe", "ShareEnum.exe", "ShellRunas.exe", "sigcheck.exe", "sigcheck64.exe", "streams.exe", "streams64.exe", "strings.exe", "strings64.exe", "sync.exe", "sync64.exe", "Sysmon.exe", "Sysmon64.exe", "Tcpvcon.exe", "Tcpview.exe", "Testlimit.exe", "Testlimit64.exe", "vmmap.exe", "Volumeid.exe", "Volumeid64.exe", "whois.exe", "whois64.exe", "Winobj.exe", "ZoomIt.exe"]})

tasklist_dic.update({'tl_infra':["LDsensors.exe", "LDpfcntrs.exe", "LDmemory.exe", "SoftMon.exe", "pds.exe", "PolicySync.exe"]})

tasklist_dic.update({'tl_knownsystemps':["svchost.exe", "System", "reg.exe", "Registry", "wininit.exe", "lsass.exe", "csrss.exe", "conhost.exe", "smss.exe", "winlogon.exe", "services.exe", "fontdrvhost.exe", "dwm.exe", "vmacthlp.exe", "spoolsv.exe", "SecurityHealthService.exe", "VGAuthService.exe", "vmtoolsd.exe", "WmiPrvSE.exe", "TPAutoConnSvc.exe", "dllhost.exe", "msdtc.exe", "SearchIndexer.exe", "sedsvc.exe", "SgrmBroker.exe", "MsMpEng.exe", "NisSrv.exe", "LogonUI.exe", "WUDFHost.exe", "audiodg.exe", "sppsvc.exe", "SearchProtocolHost.exe", "SearchFilterHost.exe", "wermgr.exe", "GoogleUpdate.exe", "SppExtComObj.exe", "sihost.exe", "taskhostw.exe", "ctfmon.exe", "RuntimeBroker.exe", "ShellExperienceHost.exe", "SearchUI.exe", "SkypeApp.exe", "ApplicationFrameHost.exe", "SkypeBackgroundHost.exe", "browser_broker.exe", "MicrosoftEdge.exe", "MicrosoftEdgeCP.exe", "LockApp.exe", "TPAutoConnect.exe", "MSASCuiL.exe", "OneDrive.exe", "cscript.exe", "Microsoft.Photos.exe", "HxTsr.exe", "backgroundTaskHost.exe"]})

tasklist_dic.update({'tl_browsers':["chrome.exe", "firefox.exe", "iexplore.exe", "MicrosoftEdgeCP.exe", "opera.exe", "msedge.exe"]})

tasklist_dic.update({'tl_exp_win':["explorer.exe", "winlogon.exe"]})

tasklist_values = list(tasklist_dic.values())
tasklist_keys = list(tasklist_dic.keys())


import re
import sys
import os.path
from datetime import date, datetime
from colorama import Fore, Back, Style, init

PsExec_Output = []

nsrlfiles = []
nsrl = os.path.exists('/usr/share/nsrl/NSRLFile.txt')
if nsrl:
    print()
    print("[*] Loading NSRL file")
    print()
    with open("/usr/share/nsrl/NSRLFile.txt", "r") as nsrlfile:
        for line in nsrlfile:
            filename = line.split(',')
            try:
                filename = filename[3].strip('"').strip('\n')
                nsrlfiles.append(filename)
            except:
                pass
        nsrlfiles = set(nsrlfiles)


def Colors(data,output):

    if not isinstance(output, str):
        output = output.decode("utf-8")

    if 'tasklist' in data:
        print()
        print("[*] AV : " + Fore.RED + "RED" + Style.RESET_ALL)
        print("[*] ADMIN : " + Fore.CYAN + "CYAN" + Style.RESET_ALL)
        print("[*] INFRA : " + Fore.BLUE + "BLUE" + Style.RESET_ALL)
        print("[*] UNKNOWN : " + Fore.MAGENTA + "MAGENTA" + Style.RESET_ALL)
        print("[*] BROWSER : " + Fore.GREEN + "GREEN" + Style.RESET_ALL)
        print("[*] KNOWNSYSTEMPS : " + Fore.WHITE + "WHITE" + Style.RESET_ALL)
        print("[*] EXPLORER/WINLOGON : " + Fore.BLUE + "BLUE" + Style.RESET_ALL)

        init(autoreset=True)
        output = output.split('\n')
        color_output = ""
        for line in output:
            try:
                process = re.findall("(.*\.exe?)", line)
                process = process[0]
            except:
                process = line.split(' ')[0]

            if process in tasklist_dic.get('tl_av'):
                line = Fore.RED + line
            elif process in tasklist_dic.get('tl_admin'):                       
                line = Fore.CYAN + line
            elif process in tasklist_dic.get('tl_infra'): 
                line = Fore.BLUE + line
            elif process in tasklist_dic.get('tl_knownsystemps'): 
                line = Fore.WHITE + line
            elif process in tasklist_dic.get('tl_browsers'): 
                line = Fore.GREEN + line
            elif process in tasklist_dic.get('tl_exp_win'): 
                line = Fore.BLUE + line
            else:
                if line == output[1]:
                    pass
                elif line == output[2]:
                    pass
                else:
                    line = Fore.MAGENTA + line

            color_output += line + Style.RESET_ALL
            color_output += line + "\n" 

        sys.stdout.write(color_output)

    elif data[:3] == "dir":

        if nsrl:
            print()
            print("[*] KNOWN WINDOWS FILE : " + Fore.WHITE + "WHITE" + Style.RESET_ALL + "\t [*] UNKNOWN FILE : " + Fore.MAGENTA + "MAGENTA" + Style.RESET_ALL)
            print()

        init(autoreset=True)
        output = output.split('\n')
        color_output = ""
        no_color_index = [0,1,2,3,4,len(output)-3,len(output)-2,len(output)-1,len(output)]
        current_year = date.today().year

        for line in output:
            try:
                if output.index(line) not in no_color_index:
                    line_date = re.findall("((^.*)  \d+:\d+)", line)
                    line_date = line_date[0]
                    if line_date != '':
                        datem = datetime.strptime(line_date[1], "%d/%m/%Y")
                        if datem.year == current_year:
                            line = line.replace(line_date[0], Fore.GREEN + line_date[0] + Style.RESET_ALL)
                        elif datem.year == current_year - 1:
                            line = line.replace(line_date[0], Fore.YELLOW + line_date[0] + Style.RESET_ALL)
                        elif datem.year <= current_year - 2:
                            line = line.replace(line_date[0], Fore.RED + line_date[0] + Style.RESET_ALL)
                    else:
                        pass

                    if '<DIR>' not in line:
                        file_bytes = re.findall("^.*?\s  (\d.*?)\s", line)
                        file_name = re.findall("^.*?\s  \d.*?\s(.*)", line)
                        file_bytes = file_bytes[0]
                        file_name = file_name[0].strip('\r')
                        if int(file_bytes.replace(',','')) <= 2000000:
                            line =  re.sub("\s\d+,?\d*\s", Fore.GREEN + " " + file_bytes + " " + Style.RESET_ALL, line)
                        elif int(file_bytes.replace(',','')) <= 10000000:
                            line = line.replace(file_bytes, Fore.YELLOW + file_bytes + Style.RESET_ALL) 
                        else:
                            line = line.replace(file_bytes, Fore.RED + file_bytes + Style.RESET_ALL)

                        if nsrlfiles != []:
                            if file_name in nsrlfiles or file_name + ".mui" in nsrlfiles:
                                line = line.replace(file_name, Fore.WHITE + file_name + Style.RESET_ALL)
                                pass
                            else:
                                line = line.replace(file_name, Fore.MAGENTA + file_name + Style.RESET_ALL)

                    else:
                        dir_path = re.findall("<DIR>.*", line)
                        dir_path = dir_path[0]
                        line = line.replace(dir_path, Fore.BLUE + dir_path + Style.RESET_ALL)
            
                color_output += line + "\n" 

            except:
                pass

        sys.stdout.write(color_output)

    elif 'netstat' in data:
        init(autoreset=True)
        output = output.split('\n')
        color_output = ""
        no_color_index = [0,1,2,3,len(output)]
        for line in output:
            if output.index(line) not in no_color_index:
                netstat_parse = re.findall("(TCP|UDP).*?(((?:[0-9]{1,3}\.){3}[0-9]{1,3})|\[::\]):(\d+)\s+(.*\w+.*|.*\d+.*|\[::\]):(.*\w+|.*\d+).*\s(LISTENING|ESTABLISHED|CLOSE_WAIT|TIME_WAIT)", line)

                if netstat_parse == []:
                    netstat_parse = re.findall("(TCP|UDP).*?(((?:[0-9]{1,3}\.){3}[0-9]{1,3})|\[.*\]|\[::1\]):(\d+)\s+(\*|.*\w+.*|.*\d+.*|\[::\]|\[::1\]):(\*|.*\w+|.*\d+).*?\s+(LISTENING|ESTABLISHED|CLOSE_WAIT|TIME_WAIT)", line)

                if netstat_parse == []:
                    netstat_parse = re.findall("(TCP|UDP).*?(((?:[0-9]{1,3}\.){3}[0-9]{1,3})|\[.*\]|\[::1\]):(\d+)\s+(\*|.*\w+.*|.*\d+.*|\[::\]|\[::1\]):(\*|.*\w+|.*\d+)(.*?)", line)

                if netstat_parse != []:
                    netstat_parse = netstat_parse[0]
                    proto = netstat_parse[0]
                    lhost = netstat_parse[1]
                    lport = netstat_parse[3]
                    rhost = netstat_parse[4]
                    rport = netstat_parse[5]
                    state = netstat_parse[6]

                    if proto == "UDP" or proto == "TCP":
                        line = line.replace(proto, Fore.WHITE + proto + Style.RESET_ALL)
                    
                    line = line.replace(lhost + ":" + lport, lhost + ":" + Fore.YELLOW + lport + Style.RESET_ALL)
                    line = line.replace(rhost + ":" + rport, rhost + ":" + Fore.YELLOW + rport + Style.RESET_ALL)

                    if lport == "0":
                        line = line.replace(lhost + ":" + Fore.YELLOW + rport + Style.RESET_ALL, lhost + ":" + Fore.BLUE + lport + Style.RESET_ALL)
                    elif rport == "0":
                        line = line.replace(rhost + ":" + Fore.YELLOW + rport + Style.RESET_ALL, rhost + ":" + Fore.BLUE + rport + Style.RESET_ALL)

                    if "0.0.0.0" in line:
                        line = line.replace("0.0.0.0", Fore.BLUE + "0.0.0.0" + Style.RESET_ALL)
                    elif "127.0.0.1" in line:
                        line = line.replace("127.0.0.1", Fore.BLUE + "127.0.0.1" + Style.RESET_ALL)
                    elif "[::]" in line:
                        line = line.replace("[::]", Fore.BLUE + "[::]" + Style.RESET_ALL)
                    elif "[::1]" in line:
                        line = line.replace("[::1]", Fore.BLUE + "[::1]" + Style.RESET_ALL)

                    if ("[" and "]") in lhost:
                        if lhost[:5] == "[fe80":
                            line = line.replace(lhost, Fore.BLUE + lhost + Style.RESET_ALL)
                        elif lhost != "[::]" and lhost != "[::1]":
                            line = line.replace(lhost, Fore.MAGENTA + lhost + Style.RESET_ALL)

                    if ("[" and "]") in rhost:
                        if rhost[:5] == "[fe80":
                            line = line.replace(rhost, Fore.BLUE + rhost + Style.RESET_ALL)
                        elif rhost != "[::]" and rhost != "[::1]":
                            line = line.replace(rhost, Fore.MAGENTA + rhost + Style.RESET_ALL)

                    if lhost != "0.0.0.0" and lhost != "127.0.0.1" and ("[" and "]") not in lhost and lhost != "*" and re.search("[a-zA-Z]", lhost) == None:
                        line = line.replace(lhost, Fore.MAGENTA + lhost + Style.RESET_ALL)

                    if rhost != "0.0.0.0" and rhost != "127.0.0.1" and ("[" and "]") not in lhost and rhost != "*" and re.search("[a-zA-Z]", rhost) == None:
                        line = line.replace(rhost, Fore.MAGENTA + rhost + Style.RESET_ALL)

                    if state == "LISTENING":
                        line = line.replace(state, Fore.BLUE + state + Style.RESET_ALL)
                    elif state == "ESTABLISHED":
                        line = line.replace(state, Fore.GREEN + state + Style.RESET_ALL)
                    elif state == "CLOSE_WAIT":
                        line = line.replace(state, Fore.RED + state + Style.RESET_ALL)
                    elif state == "TIME_WAIT":
                        line = line.replace(state, Fore.RED + state + Style.RESET_ALL)

                    if rhost == "*" and rport == "*":
                        line = line.replace(rhost + ":" + Fore.YELLOW + rport + Style.RESET_ALL, Fore.BLUE + rhost + Style.RESET_ALL + ":" + Fore.BLUE + rport + Style.RESET_ALL)

            color_output += line + "\n" 

        sys.stdout.write(color_output)

    elif data == 'smbclient_ls':

        if nsrl:
            print()
            print("[*] KNOWN WINDOWS FILE : " + Fore.WHITE + "WHITE" + Style.RESET_ALL + "\t [*] UNKNOWN FILE : " + Fore.MAGENTA + "MAGENTA" + Style.RESET_ALL)
            print()

        init(autoreset=True)
        output = output.split('\n')
        color_output = ""
        current_year = date.today().year

        for line in output:
            if line != '':
                ls_parse = re.findall("(.*?)\s?(\d+)\s+(\w{3}.*\d{4})\s(.*)", line)
                ls_parse = ls_parse[0]

            if ls_parse != [] and line != '':
                rights = ls_parse[0]
                bytes = ls_parse[1]
                ls_date = ls_parse[2]
                filename = ls_parse[3]

            if int(ls_date[-4:]) == current_year:
                line = line.replace(ls_date, Fore.GREEN + ls_date + Style.RESET_ALL)
            elif int(ls_date[-4:]) == current_year - 1:
                line = line.replace(ls_date, Fore.YELLOW + ls_date + Style.RESET_ALL)
            elif int(ls_date[-4:]) <= current_year - 2:
                line = line.replace(ls_date, Fore.RED + ls_date + Style.RESET_ALL)

            if nsrlfiles != []:
                if filename in nsrlfiles or filename + ".mui" in nsrlfiles:
                    line = line.replace(filename, Fore.WHITE + filename + Style.RESET_ALL)
                    line = line.replace(rights, Fore.WHITE + rights + Style.RESET_ALL)
                    pass
                else:
                    line = line.replace(filename, Fore.MAGENTA + filename + Style.RESET_ALL)
                    line = line.replace(rights, Fore.MAGENTA + rights + Style.RESET_ALL)

            if rights[0] == "d":
                line = line.replace(rights, Fore.BLUE + rights + Style.RESET_ALL)
                line = line.replace(filename, Fore.BLUE + filename + Style.RESET_ALL)

            if int(bytes.replace(',','')) <= 5000:
                line =  re.sub("\d+,?\d*\s\s", Fore.GREEN + bytes + "  " + Style.RESET_ALL, line)
            elif int(bytes.replace(',','')) <= 10000:
                line = line.replace(bytes, Fore.YELLOW + bytes + Style.RESET_ALL) 
            else:
                line = line.replace(bytes, Fore.RED + bytes + Style.RESET_ALL)

            color_output += line + "\n" 

        sys.stdout.write(color_output)

    else:

        sys.stdout.write(output + "\n")